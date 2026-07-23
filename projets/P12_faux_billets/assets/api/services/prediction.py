from pathlib import Path

import joblib
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_CANDIDATES = [
    BASE_DIR / "src" / "model_oncfm.joblib",
    BASE_DIR / "model_oncfm.joblib",
    BASE_DIR / "data" / "processed" / "model_oncfm.joblib",
]
EXPECTED_FEATURE_COUNT = 6
FEATURE_NAMES = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length",
]
_model = None


def _resolve_model_path() -> Path:
    for candidate in MODEL_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        "Aucun modele compatible trouve. Attendu: src/model_oncfm.joblib"
    )


def get_model():
    global _model
    if _model is None:
        model_path = _resolve_model_path()
        _model = joblib.load(model_path)
        print(f"Modele charge : {model_path.resolve()}")
    return _model


def is_model_loaded():
    try:
        return get_model() is not None
    except FileNotFoundError:
        return False


def predict_single(values):
    loaded_model = get_model()
    if len(values) != EXPECTED_FEATURE_COUNT:
        raise ValueError(f"{EXPECTED_FEATURE_COUNT} valeurs attendues, recu {len(values)}")

    sample = pd.DataFrame([np.array(values, dtype=float)], columns=FEATURE_NAMES)
    prediction = loaded_model.predict(sample)
    probabilities = loaded_model.predict_proba(sample)[0]
    proba_faux = float(probabilities[1])
    return int(prediction[0]), round(proba_faux, 3)
