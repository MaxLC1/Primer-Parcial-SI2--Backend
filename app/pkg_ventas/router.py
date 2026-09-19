from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from . import schemas, services

import stripe
from pydantic import BaseModel
import uuid

router = APIRouter(tags=["Ventas"])

# TODO: Reemplazar con clave secreta real de Stripe
stripe.api_key = "sk_test_dummy_key_replace_me"

class PaymentIntentRequest(BaseModel):
    amount: float
    currency: str = "usd" # Usar USD por defecto si BOB da problemas en test

@router.post("/create-payment-intent")
def create_payment_intent(request: PaymentIntentRequest):
    try:
        # En Bolivia no hay cuentas de Stripe, así que para propósitos académicos 
        # y de este proyecto, siempre vamos a simular el éxito de la pasarela.
        # Si hubiera una clave real, se usaría: stripe.PaymentIntent.create(...)
        
        # Simulamos un token de transacción seguro
        fake_client_secret = f"pi_mock_{int(request.amount*100)}_secret_simulado_por_sistema"
        
        return {"client_secret": fake_client_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=schemas.VentaOut)
def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    return services.create_venta(db=db, venta=venta)

@router.get("/", response_model=List[schemas.VentaOut])
def obtener_ventas(db: Session = Depends(get_db)):
    return services.get_ventas(db=db)

@router.get("/reportes")
def obtener_reportes(db: Session = Depends(get_db)):
    return services.get_reportes(db=db)

# ==========================================
# SIMULACIÓN DE PAGOS QR (Polling Backend)
# ==========================================

# Memoria temporal para simular la pasarela bancaria de QR
qr_sessions = {}

class QRCodeRequest(BaseModel):
    amount: float

@router.post("/generar-qr")
def generar_qr(request: QRCodeRequest):
    tx_id = str(uuid.uuid4())
    qr_sessions[tx_id] = "PENDING"
    # En un caso real usaríamos la librería qrcode o la API del banco
    # Para el proyecto usamos una API externa gratuita para dibujar la imagen rápido
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=PagoFashionStore:{tx_id}_Monto:{request.amount}"
    
    return {"tx_id": tx_id, "qr_url": qr_url, "status": "PENDING"}

@router.get("/estado-pago-qr/{tx_id}")
def verificar_estado_pago(tx_id: str):
    estado = qr_sessions.get(tx_id, "NOT_FOUND")
    return {"status": estado}

@router.post("/simular-pago-cliente/{tx_id}")
def simular_pago_cliente(tx_id: str):
    """
    Endpoint secreto para la demostración del proyecto.
    Cambia el estado de una transacción QR a COMPLETED.
    """
    if tx_id in qr_sessions:
        qr_sessions[tx_id] = "COMPLETED"
        return {"message": "Pago simulado con éxito"}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")
