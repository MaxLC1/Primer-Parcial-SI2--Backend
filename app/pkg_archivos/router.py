from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import uuid

router = APIRouter(tags=["Archivos"])

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    # Validar que sea imagen o modelo 3D
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp", ".glb", ".gltf"}
    ext = os.path.splitext(file.filename)[1].lower()
    
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado")
    
    # Generar un nombre único
    unique_filename = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join("uploads", unique_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"url": f"http://localhost:8000/uploads/{unique_filename}"}
