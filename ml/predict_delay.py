import joblib
import numpy as np


MODEL_PATH = "ml/models/delay_model.pkl"


def predict_delay(
    distance,
    rainfall,
    traffic,
    road_quality,
    flood_risk,
    landslide_risk
):

    model = joblib.load(
        MODEL_PATH
    )

    features = np.array([[
        distance,
        rainfall,
        traffic,
        road_quality,
        flood_risk,
        landslide_risk
    ]])

    prediction = model.predict(
        features
    )[0]

    return round(
        float(prediction),
        2
    )