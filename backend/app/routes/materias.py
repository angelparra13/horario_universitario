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
