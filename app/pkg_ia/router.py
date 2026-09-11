from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict, Any

from app.core.database import get_db
from . import services

router = APIRouter(tags=["Inteligencia Artificial"])

@router.get("/recomendaciones/{cliente_id}")
def recomendaciones(cliente_id: int, db: Session = Depends(get_db)):
    """Obtiene recomendaciones personalizadas para un cliente (RF25)."""
    return services.obtener_recomendaciones(cliente_id, db)

@router.post("/chatbot")
def chatbot(mensaje: str):
    """Interactúa con el asistente inteligente de la tienda."""
    return services.procesar_chatbot(mensaje)

@router.post("/reporte-voz")
def reporte_voz(comando: str):
    """Genera un reporte gerencial a partir de un comando de voz."""
    return services.generar_reporte_generativo(comando)
