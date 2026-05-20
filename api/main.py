from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(title="API Predicción de Severidad - Colombia")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

modelo_colombia = joblib.load(
    os.path.join(BASE_DIR, "models", "modelo_colombia.pkl")
)

modelo_antioquia = joblib.load(
    os.path.join(BASE_DIR, "models", "modelo_antioquia.pkl")
)

@app.get("/health")
def health():
    return {"status": "API funcionando correctamente"}

@app.get("/")
def home():
    return {
        "mensaje": "API de predicción de severidad de accidentes",
        "modelos_disponibles": ["colombia", "antioquia"]
    }


#NIVEL DE RIESGO

def evaluar_riesgo(probabilidad):
    """
    Clasifica el nivel de riesgo basado en la probabilidad.
    """
    if probabilidad <= 0.3:
        return "BAJO", "Baja probabilidad de accidente severo bajo estas condiciones."
    elif probabilidad <= 0.6:
        return "MEDIO", "Existe un riesgo moderado de severidad en el accidente."
    else:
        return "ALTO", "Alta probabilidad de accidente severo. Se recomienda precaución."


#ANÁLISIS CONTEXTUAL SEGUN TIPO DE VEHICULO

def analisis_contextual(df, probabilidad):
    """
    Genera un mensaje adicional basado en el tipo de vehículo.
    """
    vehiculo = df.iloc[0]['TIPO_VEHICULO']

    if vehiculo == "MOTO" and probabilidad >= 0.3:
        return "Las motocicletas presentan históricamente mayor riesgo de severidad."
    
    elif vehiculo == "CARRO" and probabilidad <= 0.5:
        return "Los automóviles suelen tener menor tasa de severidad comparados con motocicletas."
    
    else:
        return "El nivel de riesgo depende de múltiples factores como ubicación, tiempo y tipo de vehículo."



@app.post("/predict")
def predict(data: dict):
    """
    Endpoint principal de predicción.
    Permite elegir entre modelo nacional o Antioquia.
    """

    region = data.get("region", "colombia")

    df = pd.DataFrame([data])


    if "region" in df.columns:
        df = df.drop(columns=["region"])


    if region == "antioquia":
        columnas = [
            'TIPO_VEHICULO',
            'EDAD_VEHICULO',
            'AÑO',
            'MES',
            'MUNICIPIO_ACCIDENTE'
        ]
        model = modelo_antioquia

    else:
        columnas = [
            'TIPO_VEHICULO',
            'EDAD_VEHICULO',
            'AÑO',
            'MES',
            'DEPARTAMENTO_ACCIDENTE'
        ]
        model = modelo_colombia

    faltantes = [col for col in columnas if col not in df.columns]
    if faltantes:
        return {"error": f"Faltan columnas: {faltantes}"}

    df = df[columnas]

 
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]  # Probabilidad de severidad (clase 1)


    # Interpretación del resultado

    nivel_riesgo, mensaje = evaluar_riesgo(proba)
    mensaje_extra = analisis_contextual(df, proba)

    
    return {
        "region": region,
        "prediction": int(pred),
        "probabilidad_severidad (%)": round(proba * 100, 2),
        "nivel_riesgo": nivel_riesgo,
        "mensaje": mensaje,
        "analisis": mensaje_extra
    }