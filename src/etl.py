import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path)

def limpiar_datos(df):
    df = df.copy()

 
    df.columns = df.columns.str.strip().str.upper()


    for col in ['TIPO_VEHICULO', 'DEPARTAMENTO_ACCIDENTE', 'MUNICIPIO_ACCIDENTE']:
        if col in df.columns:
            df[col] = df[col].str.upper().str.strip()

    df = df.dropna(subset=['TIPO_VEHICULO'])

    return df