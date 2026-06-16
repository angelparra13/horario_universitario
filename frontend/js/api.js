/*
 * api.js — Capa de comunicación con el backend
 *
 * Este es el ÚNICO archivo que hace peticiones HTTP al backend.
 * Si mañana cambias la URL del servidor o el puerto, solo editas este archivo.
 *
 * Funciones que debes implementar aquí:
 *   - getMaterias()           → GET  /materias
 *   - crearMateria(datos)     → POST /materias
 *   - eliminarMateria(id)     → DELETE /materias/{id}
 *
 *   - getBloques()            → GET  /bloques
 *   - crearBloque(datos)      → POST /bloques
 *   - eliminarBloque(id)      → DELETE /bloques/{id}
 *
 *   - getConflictos()         → GET  /conflictos
 *
 * Todas las funciones deben:
 *   - Ser async y usar fetch()
 *   - Manejar errores de red y respuestas con código de error (404, 500, etc.)
 *   - Devolver los datos ya parseados como objetos JavaScript (no strings JSON)
 *
 * Los demás archivos JS importan estas funciones.
 * Ningún otro archivo debe usar fetch() directamente.
 */
