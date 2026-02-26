from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "ml", "model.pkl")

model = pickle.load(open(model_path, "rb"))

class Transaction(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Backend Running 🚀"}

@app.post("/predict")
def predict(data: Transaction):
    features = np.array(data.features).reshape(1, -1)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }