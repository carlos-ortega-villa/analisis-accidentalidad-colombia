# Análisis y Predicción de la Severidad en Accidentes de Tránsito en Colombia

Proyecto de analítica de datos y machine learning orientado a la identificación de patrones de accidentalidad vial y predicción de la severidad de los siniestros, con enfoque en el departamento de Antioquia.

## Objetivo

Desarrollar un modelo de aprendizaje automático capaz de predecir la severidad de accidentes de tránsito en Colombia, mediante el uso de técnicas de análisis exploratorio de datos (EDA), procesamiento ETL y modelado supervisado.

## Alcance del Proyecto

- Análisis exploratorio de datos a nivel nacional
- Enfoque específico en el departamento de Antioquia
- Construcción de indicadores de accidentalidad
- Desarrollo de modelos predictivos (Random Forest)
- Implementación de dashboard interactivo en Power BI
- Generación de mapas de calor por departamento y municipio de Antioquia

## Estructura del Proyecto
📁 data/
   ├── raw/
   ├── processed/
   ├── external/

📁 notebooks/
   ├── 01_data_understanding.ipynb
   ├── 02_eda.ipynb
   ├── 03_modeling.ipynb

📁 models/
   ├── modelo_colombia.pkl
   ├── modelo_antioquia.pkl

📁 outputs/
   ├── feature_importance.csv

📁 dashboard/
📁 api/
📄 requirements.txt
📄 README.md

## Tecnologías

- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib / Seaborn
- FastAPI
- Power BI

## Metodología

El proyecto se desarrolla bajo un enfoque híbrido basado en:

- CRISP-DM (para analítica de datos)
- AUP (Agile Unified Process) para organización iterativa

Fases implementadas:

1. Comprensión del negocio
2. Comprensión de los datos
3. Preparación de los datos (ETL)
4. Modelado
5. Evaluación
6. Visualización

## Modelo Predictivo

Se implementó un modelo de clasificación basado en Random Forest, integrando:

- Preprocesamiento con ColumnTransformer
- Codificación OneHot
- Escalado de variables numéricas
- Balanceo de clases mediante SMOTE

Se desarrollaron dos modelos:

- Modelo nacional (Colombia)
- Modelo específico (Antioquia)

## Resultados

- Identificación de variables clave en la severidad
- Generación de mapas de calor a nivel nacional y de Antioquia
- Modelos con capacidad de clasificación aceptable
- Dashboard interactivo para análisis dinámico
- Modelo predictivo funcional

## Conclusion

El proyecto demuestra cómo la aplicación de técnicas de analítica de datos y aprendizaje automático permite transformar datos históricos en información estratégica.

Los resultados obtenidos evidencian la viabilidad de utilizar modelos predictivos como apoyo a la toma de decisiones en seguridad vial.

## Datos
- El Dataset no se incluye en el repositorio debido a su tamaño, puede descargarse desde la pagina Datos Abiertos
- link: https://www.datos.gov.co/Transporte/VEHICULOS-INVOLUCRADOS-EN-UN-ACCIDENTE-DE-TRANSITO/6jmc-vaxk/about_data

## Cómo ejecutar

1. Clonar repositorio:

git clone 

2. Crear entorno virtual:

python -m venv venv

3. Activar entorno:

venv\Scripts\activate

4. Instalar dependencias:

pip install -r requirements.txt

5. Ejecutar notebooks o API

##  Autor

Carlos Alberto Ortega Villa  
Estudiante de Ingeniería de Sistemas  
Universidad Popular del Cesar