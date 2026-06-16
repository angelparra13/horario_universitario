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
