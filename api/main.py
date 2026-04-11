from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(title="API Accidentalidad Colombia")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

modelo_colombia = joblib.load(
    os.path.join(BASE_DIR, "models", "modelo_colombia.pkl")
)

modelo_antioquia = joblib.load(
    os.path.join(BASE_DIR, "models", "modelo_antioquia.pkl")
)


@app.get("/")
def home():
    return {
        "mensaje": "API de predicción de severidad de accidentes",
        "modelos": ["colombia", "antioquia"]
    }


@app.post("/predict")
def predict(data: dict):

    region = data.get("region", "colombia")

    df = pd.DataFrame([data])

    if "region" in df.columns:
        df = df.drop(columns=["region"])

    if region == "antioquia":
        columnas = [
            'TIPO_VEHICULO',
            'AÑO',
            'MES',
            'MUNICIPIO_ACCIDENTE'
        ]
        model = modelo_antioquia

    else:
        columnas = [
            'TIPO_VEHICULO',
            'AÑO',
            'MES',
            'DEPARTAMENTO_ACCIDENTE'
        ]
        model = modelo_colombia

    # validar columnas
    faltantes = [col for col in columnas if col not in df.columns]
    if faltantes:
        return {"error": f"Faltan columnas: {faltantes}"}

    df = df[columnas]

    pred = model.predict(df)[0]

    return {
        "region": region,
        "prediction": int(pred)
    }