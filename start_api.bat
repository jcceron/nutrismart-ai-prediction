@echo off
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate

echo 🚀 Iniciando servidor FastAPI en http://127.0.0.1:8000 ...
uvicorn app.main:app --reload

pause
