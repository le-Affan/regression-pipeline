from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained pipeline
pipeline = joblib.load("housing_pipeline.joblib")

app = FastAPI()

# Input schema (one sample)
class HousingInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(data: HousingInput):
    # Convert input to model format
    X = np.array([[  
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]])

    prediction = pipeline.predict(X)

    return {"prediction": float(prediction[0])}
