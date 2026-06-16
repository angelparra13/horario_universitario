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
