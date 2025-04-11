# app/model_loader.py

import numpy as np
from tensorflow.keras.models import load_model
import joblib
import os

# === Rutas relativas ===
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/modelo_adg_mlp.h5')
SCALER_PATH = os.path.join(os.path.dirname(__file__), '../models/escalador_minmax.pkl')

# === Cargar el modelo entrenado ===
modelo = load_model(MODEL_PATH, compile=False)

# === Cargar el scaler (MinMaxScaler de entrenamiento) ===
try:
    scaler = joblib.load(SCALER_PATH)
except FileNotFoundError:
    raise FileNotFoundError("❌ Archivo del escalador MinMaxScaler no encontrado. Debes exportarlo como escalador_minmax.pkl")

# === Función de predicción ===
def predecir_adg(input_data: dict) -> float:
    """
    Realiza la predicción de ADG (ganancia de peso) a partir de un diccionario con los valores de entrada.
    
    Args:
        input_data (dict): Diccionario con los campos:
            - Biomass
            - DayLengthMinutes
            - MeanVelo
            - MeanTA
            - GBD_5min
            - Walk
            - Rest
    
    Returns:
        float: Predicción de ADG en kg/día
    """

    # Orden de las variables esperadas
    features_order = [
        'Biomass',
        'DayLengthMinutes',
        'MeanVelo',
        'MeanTA',
        'GBD_5min',
        'Walk',
        'Rest'
    ]

    # Extraer y escalar en el orden correcto
    input_array = np.array([[input_data[feature] for feature in features_order]])
    input_scaled = scaler.transform(input_array)

    # Realizar predicción
    prediction = modelo.predict(input_scaled)
    return float(prediction[0][0])
