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
