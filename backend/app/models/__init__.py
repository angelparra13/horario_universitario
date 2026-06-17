"""
models/__init__.py — Marca esta carpeta como un paquete Python.
No necesita contener código.
"""

from app.models.schemas import (
    MateriaBase, MateriaCreate, MateriaRead,
    BloqueBase, BloqueCreate, BloqueRead,
)

Materia = MateriaRead
Bloque = BloqueRead
