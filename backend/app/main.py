import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from watchgod import watch
from services.Tests import test_connection_to_mongo

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto permite que cualquier origen acceda a la API
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)


# Ruta para la página de inicio
@app.get("/")
async def home():
    return {"message": "Bienvenido a la aplicación de Fastapi by sZuniga"}


# Manejo de errores 404
@app.exception_handler(HTTPException)
async def not_found(request, exc):
    return {"error": "No encontrado"}


# Manejo de errores 500
@app.exception_handler(Exception)
async def server_error(request, exc):
    return {"error": "Error interno del servidor"}

# Si deseas, puedes agregar más rutas y lógica de aplicación aquí
@app.get("/test-mongodb")
async def test_mongo():
    return {"message": test_connection_to_mongo()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)