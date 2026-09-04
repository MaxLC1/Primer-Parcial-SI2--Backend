from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FashionStore AR - API",
    description="Backend para la plataforma de comercio electrónico con vestidores virtuales AR",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modificar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de FashionStore AR"}

from app.pkg_seguridad.router import router as seguridad_router
from app.pkg_catalogo.router import router as catalogo_router
from app.pkg_sucursales.router import router as sucursales_router
from app.pkg_ventas.router import router as ventas_router

# Aquí incluiremos los routers de los paquetes más adelante:
app.include_router(seguridad_router, prefix="/api/v1/seguridad")
app.include_router(catalogo_router, prefix="/api/v1/catalogo")
app.include_router(sucursales_router, prefix="/api/v1/sucursales")
app.include_router(ventas_router, prefix="/api/v1/ventas")
