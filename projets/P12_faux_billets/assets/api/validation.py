from api.services.prediction import FEATURE_NAMES
import pandas as pd


FEATURE_BOUNDS = {
    "diagonal": (160.0, 180.0),
    "height_left": (95.0, 115.0),
    "height_right": (95.0, 115.0),
    "margin_low": (0.0, 10.0),
    "margin_up": (0.0, 10.0),
    "length": (100.0, 125.0),
}


def valider_billet(data: dict) -> None:
    missing_columns = [feature for feature in FEATURE_NAMES if feature not in data]
    if missing_columns:
        raise ValueError(f"Champs manquants: {', '.join(missing_columns)}")

    for feature in FEATURE_NAMES:
        value = data[feature]
        if pd.isna(value):
            continue
        low, high = FEATURE_BOUNDS[feature]
        try:
            numeric_value = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Valeur non numerique pour {feature}: {value}") from exc
        if not low <= numeric_value <= high:
            raise ValueError(
                f"Valeur hors bornes pour {feature}: {numeric_value} "
                f"(attendu entre {low} et {high})"
            )