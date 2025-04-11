# run_model_test.py

from app.model_loader import predecir_adg

# Simulación de datos reales del animal
entrada = {
    'Biomass': 3600,
    'DayLengthMinutes': 1390,
    'MeanVelo': 17.4,
    'MeanTA': 30.8,
    'GBD_5min': 10.5,
    'Walk': 420,
    'Rest': 580
}

resultado = predecir_adg(entrada)

print(f"✅ Ganancia diaria predicha: {resultado:.4f} kg/día")
