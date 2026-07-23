import io

import pandas as pd
import pytest
from sklearn.metrics import f1_score

from api.services.prediction import FEATURE_NAMES


@pytest.mark.anyio
async def test_health_retourne_200_et_cles(client):
	response = await client.get("/health")

	assert response.status_code == 200
	payload = response.json()
	assert "model_loaded" in payload
	assert "version" in payload
	assert payload["status"] == "ok"
	assert payload["model_loaded"] is True


@pytest.mark.anyio
async def test_predict_billet_vrai_retourne_200(client):
	payload_valide = {
		"diagonal": 171.81,
		"height_left": 104.86,
		"height_right": 104.95,
		"margin_low": 4.52,
		"margin_up": 2.89,
		"length": 112.83,
	}

	response = await client.post("/predict", json=payload_valide)

	assert response.status_code == 200
	payload = response.json()
	assert {"prediction", "is_genuine", "proba_vrai", "proba_faux"}.issubset(payload)
	assert payload["prediction"] == "VRAI"
	assert abs((payload["proba_vrai"] + payload["proba_faux"]) - 1.0) < 0.01


@pytest.mark.anyio
async def test_predict_retourne_422_si_champs_manquants(client):
	# Payload incomplet: Pydantic doit rejeter la requete en 422.
	payload_invalide = {
		"diagonale_mm": 171.81,
		"hauteur_gauche_mm": 104.86,
	}

	response = await client.post("/predict", json=payload_invalide)
	assert response.status_code == 422


@pytest.mark.anyio
async def test_predict_retourne_422_si_valeur_hors_bornes(client):
	payload_invalide = {
		"diagonal": -171.81,
		"height_left": 104.86,
		"height_right": 104.95,
		"margin_low": 4.52,
		"margin_up": 2.89,
		"length": 112.83,
	}

	response = await client.post("/predict", json=payload_invalide)
	assert response.status_code == 422


@pytest.mark.anyio
async def test_predict_batch_valide_retourne_200(client):
	contenu_csv = "diagonal;height_left;height_right;margin_low;margin_up;length\n"
	contenu_csv += "171.81;104.86;104.95;4.52;2.89;112.83\n"
	fichier = io.BytesIO(contenu_csv.encode("utf-8"))

	response = await client.post(
		"/predict/batch",
		files={"file": ("billets.csv", fichier, "text/csv")},
	)

	assert response.status_code == 200
	payload = response.json()
	assert payload["rows"] == 1
	assert len(payload["predictions"]) == 1
	assert {"index", "prediction", "proba_vrai", "proba_faux"}.issubset(
		payload["predictions"][0]
	)


@pytest.mark.anyio
async def test_predict_batch_accepte_csv_avec_virgules(client):
	contenu_csv = "diagonal,height_left,height_right,margin_low,margin_up,length\n"
	contenu_csv += "171.81,104.86,104.95,4.52,2.89,112.83\n"
	fichier = io.BytesIO(contenu_csv.encode("utf-8"))

	response = await client.post(
		"/predict/batch",
		files={"file": ("billets.csv", fichier, "text/csv")},
	)

	assert response.status_code == 200
	payload = response.json()
	assert payload["rows"] == 1
	assert len(payload["predictions"]) == 1


@pytest.mark.anyio
async def test_predict_batch_accepte_billets_csv_avec_valeurs_manquantes(client):
	with open("data/raw/billets.csv", "rb") as fichier:
		response = await client.post(
			"/predict/batch",
			files={"file": ("billets.csv", fichier, "text/csv")},
		)

	assert response.status_code == 200
	payload = response.json()
	assert payload["rows"] == 1500
	assert len(payload["predictions"]) == 1500
	assert payload["summary"]["actual_counts"] == {"vrai": 1000, "faux": 500}
	assert payload["summary"]["predicted_counts"] == {"vrai": 1004, "faux": 496}
	assert payload["summary"]["errors"]["total"] == 12
	assert payload["summary"]["errors"]["rate"] == 0.008


@pytest.mark.anyio
async def test_predict_batch_retourne_400_si_colonnes_invalides(client):
	contenu_csv = "diagonal;height_left;height_right;margin_low;margin_up\n"
	contenu_csv += "171.81;104.86;104.95;4.52;2.89\n"
	fichier = io.BytesIO(contenu_csv.encode("utf-8"))

	response = await client.post(
		"/predict/batch",
		files={"file": ("billets.csv", fichier, "text/csv")},
	)

	assert response.status_code == 400
	assert "Colonnes manquantes" in response.json()["detail"]


@pytest.mark.anyio
async def test_predict_batch_retourne_422_sans_fichier(client):
	response = await client.post("/predict/batch")
	assert response.status_code == 422


def test_f1_non_regression(model):
	df = pd.read_csv("data/raw/billets.csv", sep=";")
	features = df[FEATURE_NAMES]
	y_true = (~df["is_genuine"].astype(bool)).astype(int)

	y_pred = model.predict(features)
	f1 = f1_score(y_true, y_pred, average="macro")

	assert f1 >= 0.97, f"F1 macro trop bas : {f1:.4f} (seuil : 0.97)"
