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
