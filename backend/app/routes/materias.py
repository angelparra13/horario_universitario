"""
routes/materias.py — Endpoints HTTP relacionados con materias.

Define las rutas de la API para el recurso "materia":
  POST   /materias           → Crear una nueva materia
  GET    /materias           → Listar todas las materias registradas
  DELETE /materias/{id}      → Eliminar una materia por su ID

Responsabilidades de este archivo:
  - Recibir la petición HTTP
  - Validar los datos de entrada (FastAPI lo hace automáticamente con schemas)
  - Llamar al servicio correspondiente en horario_service.py
  - Devolver la respuesta con el código HTTP correcto (200, 201, 404, etc.)

NO debe contener lógica de negocio.
Si necesitas hacer algo más que llamar a un servicio, ese código
va en services/, no aquí.
"""

from fastapi import APIRouter, HTTPException
from app.schemas import MateriaCreate, MateriaRead
from app.services import materia_service

router = APIRouter(prefix="/materias", tags=["materias"])


@router.post("/", response_model=MateriaRead, status_code=201)
def create_materia(materia: MateriaCreate):
    try:
        return materia_service.create_materia(materia)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[MateriaRead])
def list_materias():
    return materia_service.list_materias()


@router.delete("/{materia_id}", status_code=204)
def delete_materia(materia_id: int):
    try:
        materia_service.delete_materia(materia_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
