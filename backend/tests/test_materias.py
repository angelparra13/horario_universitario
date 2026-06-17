"""
test_materias.py — Pruebas para los endpoints y la lógica de materias.

Aquí verificas que el sistema se comporta correctamente al operar con materias.

Casos que debes probar:
  1. Crear una materia con datos válidos → debe guardarse correctamente
  2. Intentar crear una materia sin nombre → debe fallar con error claro
  3. Listar materias cuando no hay ninguna → debe devolver lista vacía
  4. Listar materias después de haber creado varias → deben aparecer todas
  5. Eliminar una materia que existe → debe eliminarse y no aparecer en la lista
  6. Eliminar una materia que no existe → debe devolver error 404
  7. Eliminar una materia verifica que sus bloques también se eliminen

Cómo correr las pruebas:
  pytest tests/test_materias.py

Consejo: escribe primero los casos como comentarios, luego impleméntalos
uno por uno. No intentes escribir todas las pruebas a la vez.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_materia_valida():
    response = client.post("/materias/", json={"nombre": "Matemáticas"})
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Matemáticas"
    assert "id" in data

def test_crear_materia_sin_nombre():
    response = client.post("/materias/", json={})
    assert response.status_code == 422  # FastAPI devuelve 422 para datos inválidos

def test_listar_materias_vacia():
    response = client.get("/materias/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_listar_materias_despues_de_crear():
    client.post("/materias/", json={"nombre": "Física"})
    client.post("/materias/", json={"nombre": "Química"})
    
    response = client.get("/materias/")
    assert response.status_code == 200
    data = response.json()
    nombres = [m["nombre"] for m in data]
    assert "Física" in nombres
    assert "Química" in nombres

def test_eliminar_materia_existente():
    response = client.post("/materias/", json={"nombre": "Historia"})
    materia_id = response.json()["id"]
    
    delete_response = client.delete(f"/materias/{materia_id}")
    assert delete_response.status_code == 204
    
    list_response = client.get("/materias/")
    data = list_response.json()
    ids = [m["id"] for m in data]
    assert materia_id not in ids

def test_eliminar_materia_no_existente():
    response = client.delete("/materias/9999")  # ID que no existe
    assert response.status_code == 404

def test_eliminar_materia_con_bloques():
    # Crear materia
    response = client.post("/materias/", json={"nombre": "Geografía"})
    materia_id = response.json()["id"]
    
    # Crear bloque asociado a esa materia
    bloque_response = client.post("/bloques/", json={
        "id_materia": materia_id,
        "dia": "Lunes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00"
    })
    bloque_id = bloque_response.json()["id"]
    
    # Eliminar la materia
    delete_response = client.delete(f"/materias/{materia_id}")
    assert delete_response.status_code == 204
    
    # Verificar que el bloque también se eliminó
    bloques_response = client.get("/bloques/")
    bloques_data = bloques_response.json()
    bloque_ids = [b["id"] for b in bloques_data]
    assert bloque_id not in bloque_ids
