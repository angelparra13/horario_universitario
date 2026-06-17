"""
schemas.py — Define la forma (estructura) de los datos del sistema.

Aquí se declaran los modelos de datos usando clases de Pydantic.
FastAPI los usa automáticamente para:
  - Validar los datos que llegan en las peticiones (request body)
  - Validar los datos que devuelve la API (response)
  - Generar documentación automática en /docs

Modelos que debes definir aquí:
  - Materia:
      nombre (str, obligatorio)
      codigo (str, opcional)
      creditos (int, opcional)
      color (str, opcional — ej. "#FF5733")

  - Bloque:
      id_materia (str, obligatorio — referencia a la materia)
      dia (str, obligatorio — ej. "Lunes")
      hora_inicio (str, obligatorio — formato "HH:MM")
      hora_fin (str, obligatorio — formato "HH:MM")
      salon (str, opcional)

  - MateriaConBloques:
      Combinación de Materia + lista de sus Bloques.
      Útil para respuestas que devuelven todo junto.

Regla: este archivo solo describe datos. No tiene lógica ni accede al disco.
"""

from pydantic import BaseModel, Field

class MateriaBase(BaseModel):
    nombre: str = Field(..., example="Matemáticas")
    codigo: str | None = Field(None, example="MAT101")
    creditos: int | None = Field(None, example=4)
    color: str | None = Field(None, example="#FF5733")

class BloqueBase(BaseModel):
    id_materia: int = Field(..., example=1)
    dia: str = Field(..., example="Lunes")
    hora_inicio: str = Field(..., example="08:30")
    hora_fin: str = Field(..., example="10:00")
    salon: str | None = Field(None, example="Aula 101")

class MateriaCreate(MateriaBase):
    pass

class BloqueCreate(BloqueBase):
    pass

class MateriaRead(MateriaBase):
    id: int = Field(..., example=1)
    bloques: list[BloqueBase] = Field(default=[], example=[{"id_materia": 1, "dia": "Lunes", "hora_inicio":
                                                            "08:30", "hora_fin": "10:00", "salon": "Aula 101"}])

class BloqueRead(BloqueBase):
    id: int = Field(..., example=1)