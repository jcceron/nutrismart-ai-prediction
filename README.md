# 🧠 NutriSmart AI – HU-06: Predicción de Conversión Alimenticia

Este repositorio contiene el desarrollo de la Historia de Usuario HU-06 del proyecto NutriSmart AI. El objetivo es construir un modelo basado en redes neuronales para predecir la **ganancia diaria de peso (ADG)** en bovinos de pastoreo libre, utilizando variables de comportamiento de forrajeo y condiciones ambientales.

---

## 🎯 Objetivo del Proyecto

Desarrollar una red neuronal capaz de predecir la eficiencia de conversión alimenticia del ganado mediante el análisis de datos de comportamiento, temperatura, humedad y calidad de pasto (NDVI). Esto permitirá la formulación dinámica y precisa de dietas balanceadas para mejorar la rentabilidad y sostenibilidad de la producción ganadera.

---

## 🧩 Dataset Utilizado

- 📄 `Moo2019-20_dailymetrics_database.csv`
- Fuente: [Data.gov](https://catalog.data.gov/dataset/data-from-can-measurements-of-foraging-behaviour-predict-variation-in-weight-gains-of-free-f45bb)
- Variables seleccionadas:
  - `Grazing_min`, `Steps`, `Distance_m`, `GrazingSpeed_m_s`, `TurnAngle`, `Resting_min`, `Ruminating_min`
  - `Humidity`, `Temp`, `ForageNDVI`, `BiomassEst`
  - `ADG_INT` (Variable objetivo)

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.11
- **Frameworks:** TensorFlow, Keras, Scikit-learn
- **API Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Visualización y EDA:** Pandas, Seaborn, Matplotlib
- **Editor:** Visual Studio Code
- **Control de versiones:** Git + GitHub
- **Ambiente local:** venv + `.gitignore` + Docker (opcional)

---

## 🗂️ Estructura del Proyecto



---

## 🚀 Cómo Ejecutar Localmente

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/nutrismart-ai-prediction.git
cd nutrismart-ai-prediction

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar FastAPI (más adelante)
uvicorn app.main:app --reload

# Ejecutar Jupyter Notebook
jupyter notebook

# Métricas esperadas del modelo
R² ≥ 0.90
MAE y RMSE mínimos
Tiempo de inferencia < 2 segundos

# Autores
María Alejandra Benítez
Paula Andrea Díaz Pinzón
Juan Carlos Cerón Lombana

Maestría en Ciencia de Datos y Sistemas Inteligentes
Universidad Santo Tomás – Bucaramanga

# Licencia
MIT License – Libre para uso académico y de investigación