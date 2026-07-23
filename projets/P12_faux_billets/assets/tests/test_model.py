from pathlib import Path

import joblib
import pytest

from api.validation import valider_billet


MODEL_PATH = Path("src/model_oncfm.joblib")

BILLET_VRAI = [[171.81, 104.86, 104.95, 4.52, 2.89, 112.83]]
BILLET_FAUX = [[172.28, 103.95, 103.91, 4.78, 3.31, 111.40]]


def test_modele_existe():
	assert MODEL_PATH.exists()


def test_modele_se_charge():
	modele = joblib.load(MODEL_PATH)
	assert modele is not None


def test_modele_expose_predict_appelable():
	modele = joblib.load(MODEL_PATH)
	assert callable(modele.predict)


def test_prediction_billet_vrai():
	modele = joblib.load(MODEL_PATH)
	prediction = modele.predict(BILLET_VRAI)
	assert int(prediction[0]) == 0


def test_prediction_billet_faux():
	modele = joblib.load(MODEL_PATH)
	prediction = modele.predict(BILLET_FAUX)
	assert int(prediction[0]) == 1


def test_predict_proba_format():
	modele = joblib.load(MODEL_PATH)
	proba = modele.predict_proba(BILLET_VRAI)
	assert proba.shape == (1, 2)
	assert 0.0 <= proba[0][0] <= 1.0
	assert 0.0 <= proba[0][1] <= 1.0


def test_validation_refuse_champ_manquant():
	with pytest.raises(ValueError, match="Champs manquants"):
		valider_billet({"diagonal": 171.81})


def test_validation_refuse_dict_vide():
	with pytest.raises(ValueError, match="Champs manquants"):
		valider_billet({})


def test_validation_accepte_donnees_valides():
	valider_billet(
		{
			"diagonal": 171.81,
			"height_left": 104.86,
			"height_right": 104.95,
			"margin_low": 4.52,
			"margin_up": 2.89,
			"length": 112.83,
		}
	)
