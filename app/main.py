from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from app.model_loader import predecir_adg

# === Inicialización de FastAPI ===
app = FastAPI(
    title="NutriSmart AI - API de Predicción de Ganancia de Peso (ADG)",
    description="""
    Esta API permite predecir la **ganancia diaria de peso** en bovinos de pastoreo extensivo,
    utilizando un modelo de red neuronal entrenado con datos reales de comportamiento de pastoreo,
    velocidad, duración del día, y biomasa disponible.

    ✅ Ideal para integrar en herramientas de nutrición y gestión ganadera inteligente.
    """,
    version="1.0.0"
)

# === Montaje de carpetas frontend ===
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

# === Esquema de entrada para el endpoint API REST ===
class DatosAnimal(BaseModel):
    biomasa_disponible: float = Field(..., description="Estimación de biomasa forrajera disponible (kg de MS por hectárea)")
    duracion_dia_minutos: float = Field(..., description="Duración total del día con datos válidos (en minutos)")
    velocidad_promedio_pastoreo: float = Field(..., description="Velocidad promedio del animal mientras pasta (m/min)")
    angulo_promedio_giro: float = Field(..., description="Ángulo de giro promedio del animal durante el pastoreo (°)")
    duracion_media_sesion_pastoreo: float = Field(..., description="Duración media de cada sesión de pastoreo (min)")
    pasos_caminando: float = Field(..., description="Conteo de pasos o intervalos de 4 segundos caminando")
    tiempo_descanso: float = Field(..., description="Conteo de intervalos de 4 segundos en reposo")

# === Ruta visual (formulario) ===
@app.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# === Endpoint visual para enviar datos del formulario ===
@app.post("/predecir", response_class=HTMLResponse)
def predecir_web(
    request: Request,
    biomasa_disponible: float = Form(...),
    duracion_dia_minutos: float = Form(...),
    velocidad_promedio_pastoreo: float = Form(...),
    angulo_promedio_giro: float = Form(...),
    duracion_media_sesion_pastoreo: float = Form(...),
    pasos_caminando: int = Form(...),
    tiempo_descanso: int = Form(...)
):
    entrada = {
        'Biomass': biomasa_disponible,
        'DayLengthMinutes': duracion_dia_minutos,
        'MeanVelo': velocidad_promedio_pastoreo,
        'MeanTA': angulo_promedio_giro,
        'GBD_5min': duracion_media_sesion_pastoreo,
        'Walk': pasos_caminando,
        'Rest': tiempo_descanso
    }
    resultado = predecir_adg(entrada)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediccion": f"{resultado:.4f} kg/día"
    })

# === Endpoint REST para integración programática (POST .http / frontend JS) ===
@app.post("/predecir_adg/", tags=["Predicción ADG"])
def predecir_api(datos: DatosAnimal):
    entrada = {
        'Biomass': datos.biomasa_disponible,
        'DayLengthMinutes': datos.duracion_dia_minutos,
        'MeanVelo': datos.velocidad_promedio_pastoreo,
        'MeanTA': datos.angulo_promedio_giro,
        'GBD_5min': datos.duracion_media_sesion_pastoreo,
        'Walk': datos.pasos_caminando,
        'Rest': datos.tiempo_descanso
    }
    resultado = predecir_adg(entrada)
    return {
        "ganancia_diaria_predicha_kg": round(resultado, 4),
        "modelo": "MLP Optimizado - NutriSmart AI"
    }
