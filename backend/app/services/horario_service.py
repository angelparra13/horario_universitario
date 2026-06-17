"""
horario_service.py — Lógica de negocio principal del sistema.

Este archivo es el núcleo del backend. Contiene todas las operaciones
sobre los datos: leer, guardar, buscar, agregar y eliminar.

Funciones que debes implementar aquí:
  - cargar_datos()
      Lee data/horario.json y devuelve el estado actual como dict.
      Si el archivo no existe, devuelve estructura vacía: {"materias": [], "bloques": []}.

  - guardar_datos(datos)
      Sobreescribe data/horario.json con el dict actualizado.

  - agregar_materia(materia)
      Genera un ID único para la materia, la añade a la lista y guarda.

  - obtener_materias()
      Devuelve la lista de materias desde el JSON.

  - eliminar_materia(id)
      Elimina la materia y todos sus bloques asociados, luego guarda.

  - agregar_bloque(bloque)
      Verifica que la materia referenciada existe, genera ID, añade y guarda.

  - obtener_bloques()
      Devuelve todos los bloques registrados.

  - eliminar_bloque(id)
      Elimina el bloque por ID y guarda.

Regla: este archivo no sabe nada de HTTP.
No maneja peticiones ni respuestas. Solo trabaja con datos y el archivo JSON.
"""

import json
import os
from app.models import Materia, Bloque

DATA_FILE = "data/horario.json"

def cargar_datos() -> dict:
    if not os.path.exists(DATA_FILE):
        return {"materias": [], "bloques": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def guardar_datos(datos: dict):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)

def agregar_materia(materia: Materia) -> Materia:
    datos = cargar_datos()
    nueva_id = max((m["id"] for m in datos["materias"]), default=0) + 1
    materia_dict = materia.dict()
    materia_dict["id"] = nueva_id
    datos["materias"].append(materia_dict)
    guardar_datos(datos)
    return Materia(**materia_dict)

def obtener_materias() -> list[Materia]:
    datos = cargar_datos()
    return [Materia(**m) for m in datos["materias"]]

def eliminar_materia(materia_id: int):
    datos = cargar_datos()
    datos["materias"] = [m for m in datos["materias"] if m["id"] != materia_id]
    datos["bloques"] = [b for b in datos["bloques"] if b["id_materia"] != materia_id]
    guardar_datos(datos)

def agregar_bloque(bloque: Bloque) -> Bloque:
    datos = cargar_datos()
    if not any(m["id"] == bloque.id_materia for m in datos["materias"]):
        raise ValueError("Materia no encontrada para el bloque")
    nueva_id = max((b["id"] for b in datos["bloques"]), default=0) + 1
    bloque_dict = bloque.dict()
    bloque_dict["id"] = nueva_id
    datos["bloques"].append(bloque_dict)
    guardar_datos(datos)
    return Bloque(**bloque_dict)

def obtener_bloques() -> list[Bloque]:
    datos = cargar_datos()
    return [Bloque(**b) for b in datos["bloques"]]

def eliminar_bloque(bloque_id: int):
    datos = cargar_datos()
    datos["bloques"] = [b for b in datos["bloques"] if b["id"] != bloque_id]
    guardar_datos(datos)
