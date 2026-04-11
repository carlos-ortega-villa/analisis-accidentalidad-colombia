from etl import cargar_datos, limpiar_datos
from features import crear_variables_fecha, crear_severidad

# cargar
df = cargar_datos("../data/raw/VEHICULOS_INV_EN_UN_ACCIDENTE.csv")

# limpiar
df = limpiar_datos(df)

# features
df = crear_variables_fecha(df)
df = crear_severidad(df)

# guardar
df.to_csv("../data/processed/dataset_limpio.csv", index=False)

print("Dataset limpio generado correctamente")