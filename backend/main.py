from fastapi import FastAPI
from pydantic import BaseModel

from ml.predict_delay import predict_delay


app = FastAPI(
    title="NER Smart Logistics AI API",
    version="1.0"
)


@app.get("/")
def root():

    return {
        "message": "NER Smart Logistics AI API",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


class DelayRequest(BaseModel):

    distance: float
    rainfall: float
    traffic: float
    road_quality: float
    flood_risk: float
    landslide_risk: float


@app.post("/predict-delay")
def delay_prediction(
    request: DelayRequest
):

    delay = predict_delay(
        request.distance,
        request.rainfall,
        request.traffic,
        request.road_quality,
        request.flood_risk,
        request.landslide_risk
    )

    return {
        "predicted_delay_minutes": delay
    }