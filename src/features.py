import pandas as pd

def crear_variables_fecha(df):
    df = df.copy()

    df['FECHA'] = pd.to_datetime(df['FECHA_ACCIDENTE'], errors='coerce')

    df['AÑO'] = df['FECHA'].dt.year
    df['MES'] = df['FECHA'].dt.month

    return df


def crear_severidad(df):
    df = df.copy()

    df['SEVERIDAD'] = df['GRAVEDAD_ACCIDENTE'].apply(
        lambda x: 1 if 'MUERTO' in str(x).upper() else 0
    )

    return df