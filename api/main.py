from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/modelo_severidad.pkl")

@app.get("/")
def home():
    return {"mensaje": "API de predicción de severidad de accidentes"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return {
        "prediccion": int(prediction),
        "descripcion": "Fatal" if prediction == 1 else "No fatal"
    }