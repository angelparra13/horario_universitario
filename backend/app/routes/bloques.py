"""
routes/bloques.py — Endpoints HTTP relacionados con bloques de horario.

Define las rutas de la API para el recurso "bloque":
  POST   /bloques            → Crear un nuevo bloque y asignarlo a una materia
  GET    /bloques            → Listar todos los bloques registrados
  DELETE /bloques/{id}       → Eliminar un bloque por su ID
  GET    /conflictos         → Devolver la lista de bloques que se solapan

Responsabilidades de este archivo:
  - Recibir la petición HTTP
  - Llamar al servicio correspondiente (horario_service.py o conflictos.py)
  - Devolver la respuesta con el código HTTP correcto

NO debe contener lógica de negocio.
"""

from fastapi import APIRouter, HTTPException
from app.schemas import BloqueCreate, BloqueRead
from app.services import bloque_service, conflicto_service

router = APIRouter(prefix="/bloques", tags=["bloques"])

@router.post("/", response_model=BloqueRead, status_code=201)
def create_bloque(bloque: BloqueCreate):
    try:
        return bloque_service.create_bloque(bloque)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/", response_model=list[BloqueRead])
def list_bloques():
    return bloque_service.list_bloques()

@router.delete("/{bloque_id}", status_code=204)
def delete_bloque(bloque_id: int):
    try:
        bloque_service.delete_bloque(bloque_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/conflictos", response_model=list[BloqueRead])
def list_conflictos():
    return conflicto_service.list_conflictos()