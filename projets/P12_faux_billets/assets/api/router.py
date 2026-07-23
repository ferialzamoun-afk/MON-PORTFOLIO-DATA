import io

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from api.services.prediction import FEATURE_NAMES, is_model_loaded, predict_single
from api.validation import valider_billet


router = APIRouter()


class PredictionInput(BaseModel):
	diagonal: float = Field(..., ge=160.0, le=180.0, description="Diagonale du billet en millimetres", examples=[171.81])
	height_left: float = Field(..., ge=95.0, le=115.0, description="Hauteur gauche en millimetres", examples=[104.86])
	height_right: float = Field(..., ge=95.0, le=115.0, description="Hauteur droite en millimetres", examples=[104.95])
	margin_low: float = Field(..., ge=0.0, le=10.0, description="Marge basse en millimetres", examples=[4.52])
	margin_up: float = Field(..., ge=0.0, le=10.0, description="Marge haute en millimetres", examples=[2.89])
	length: float = Field(..., ge=100.0, le=125.0, description="Longueur du billet en millimetres", examples=[112.83])

	model_config = {
		"json_schema_extra": {
			"example": {
				"diagonal": 171.81,
				"height_left": 104.86,
				"height_right": 104.95,
				"margin_low": 4.52,
				"margin_up": 2.89,
				"length": 112.83,
			}
		}
	}


class PredictionOutput(BaseModel):
	prediction: str = Field(..., examples=["VRAI"])
	is_genuine: bool = Field(..., examples=[True])
	proba_vrai: float = Field(..., ge=0.0, le=1.0, examples=[0.96])
	proba_faux: float = Field(..., ge=0.0, le=1.0, examples=[0.04])


class BatchPredictionOutput(PredictionOutput):
	index: int = Field(..., ge=0, examples=[0])


class BatchOutput(BaseModel):
	rows: int = Field(..., ge=0, examples=[1])
	summary: dict | None = Field(default=None, description="Synthese disponible si le CSV contient la colonne is_genuine")
	predictions: list[BatchPredictionOutput]


class HealthOutput(BaseModel):
	status: str = Field(..., examples=["ok"])
	model_loaded: bool = Field(..., examples=[True])
	version: str = Field(..., examples=["1.0.0"])


def _format_prediction(index: int, values: list[float]) -> dict:
	prediction, proba_faux = predict_single(values)
	is_genuine = prediction == 0
	return {
		"index": index,
		"prediction": "VRAI" if is_genuine else "FAUX",
		"is_genuine": is_genuine,
		"proba_vrai": round(1.0 - proba_faux, 3),
		"proba_faux": round(proba_faux, 3),
	}


def _build_reference_summary(df: pd.DataFrame, predictions: list[dict]) -> dict | None:
	if "is_genuine" not in df.columns:
		return None

	y_true = (~df["is_genuine"].astype(bool)).astype(int)
	y_pred = pd.Series([0 if item["is_genuine"] else 1 for item in predictions], index=df.index)
	errors = y_true != y_pred
	false_positive = int(((y_true == 0) & (y_pred == 1)).sum())
	false_negative = int(((y_true == 1) & (y_pred == 0)).sum())

	return {
		"reference_available": True,
		"actual_counts": {
			"vrai": int((y_true == 0).sum()),
			"faux": int((y_true == 1).sum()),
		},
		"predicted_counts": {
			"vrai": int((y_pred == 0).sum()),
			"faux": int((y_pred == 1).sum()),
		},
		"errors": {
			"total": int(errors.sum()),
			"rate": round(float(errors.mean()), 4),
			"vrais_predits_faux": false_positive,
			"faux_predits_vrais": false_negative,
		},
	}


@router.get("/", tags=["General"], summary="Message d'accueil")
def read_root():
	return {
		"message": (
			"Bienvenue sur l'API de detection de faux billets. "
			"Utilisez l'endpoint /predict pour classer un billet."
		)
	}


@router.get("/health", response_model=HealthOutput, tags=["Monitoring"], summary="Verifier l'etat de l'API et du modele")
def read_health():
	return {
		"status": "ok",
		"model_loaded": is_model_loaded(),
		"version": "1.0.0",
	}


@router.post(
	"/predict",
	response_model=PredictionOutput,
	tags=["Prediction"],
	summary="Predire un billet",
	description="Retourne la classe predite et les probabilites pour un billet decrit par 6 mesures physiques.",
)
def predict(data: PredictionInput):
	valider_billet(data.model_dump())
	result = _format_prediction(
		0,
		[
			data.diagonal,
			data.height_left,
			data.height_right,
			data.margin_low,
			data.margin_up,
			data.length,
		],
	)
	result.pop("index")
	return result


@router.post(
	"/predict/batch",
	response_model=BatchOutput,
	tags=["Prediction"],
	summary="Predire plusieurs billets depuis un CSV",
	description="Accepte un fichier CSV separe par point-virgule ou par virgule, avec les 6 colonnes attendues.",
)
def predict_batch(
	file: UploadFile = File(
		...,
		description="Fichier CSV contenant les colonnes diagonal, height_left, height_right, margin_low, margin_up et length",
	)
):
	contenu = file.file.read()

	try:
		df = pd.read_csv(io.StringIO(contenu.decode("utf-8-sig")), sep=None, engine="python")
	except Exception as exc:
		raise HTTPException(status_code=400, detail=f"CSV invalide: {exc}") from exc

	missing_columns = [column for column in FEATURE_NAMES if column not in df.columns]
	if missing_columns:
		raise HTTPException(
			status_code=400,
			detail=f"Colonnes manquantes: {', '.join(missing_columns)}",
		)

	predictions = []
	try:
		for index, row in df[FEATURE_NAMES].iterrows():
			valider_billet(row.to_dict())
			predictions.append(_format_prediction(int(index), row.tolist()))
	except Exception as exc:
		raise HTTPException(status_code=400, detail=f"Prediction impossible: {exc}") from exc

	return {
		"rows": int(len(df)),
		"summary": _build_reference_summary(df, predictions),
		"predictions": predictions,
	}
