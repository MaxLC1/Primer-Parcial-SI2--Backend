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

def procesar_chatbot(mensaje: str):
    # Lógica mock para el chatbot
    return {
        "respuesta": "Hola, soy el asistente virtual de FashionStore. ¿En qué puedo ayudarte con tu compra?"
    }

def generar_reporte_generativo(comando_voz: str):
    # Lógica mock
    return {
        "reporte": "Las ventas de la temporada actual han subido un 15%. La prenda más reservada es la chaqueta de cuero."
    }
