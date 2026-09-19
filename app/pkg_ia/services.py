from sqlalchemy.orm import Session
from fastapi import HTTPException
# Este servicio eventualmente conectaría con un modelo de IA (OpenAI, Gemini, etc.)

def obtener_recomendaciones(cliente_id: int, db: Session):
    # Lógica mock para MVP
    return {
        "cliente_id": cliente_id,
        "recomendaciones": [
            {"producto_id": 1, "motivo": "Basado en tus compras de verano"},
            {"producto_id": 2, "motivo": "Popular en tu ciudad"}
        ]
    }

from sqlalchemy import func
from app.pkg_sucursales.models import Inventario

def procesar_chatbot(mensaje: str, db: Session):
    mensaje_lower = mensaje.lower()
    
    # Lógica para consultas de stock total acumulado
    if "stock" in mensaje_lower or "cuántos" in mensaje_lower or "cuantos" in mensaje_lower or "inventario" in mensaje_lower:
        total_stock = db.query(func.sum(Inventario.cantidad)).scalar() or 0
        return {
            "respuesta": f"Actualmente tenemos un stock total acumulado de {total_stock} prendas en todas nuestras sucursales."
        }
        
    # Lógica mock para otros comandos
    return {
        "respuesta": "Hola, soy el asistente virtual de FashionStore. ¿En qué puedo ayudarte con tu compra? (Prueba preguntando por el stock)."
    }

def generar_reporte_generativo(comando_voz: str):
    # Lógica mock
    return {
        "reporte": "Las ventas de la temporada actual han subido un 15%. La prenda más reservada es la chaqueta de cuero."
    }
