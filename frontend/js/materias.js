/*
 * materias.js — Renderizado del panel de materias en index.html
 *
 * Este archivo se encarga de construir el HTML para mostrar
 * la lista de materias registradas y las alertas de conflicto.
 * No hace peticiones HTTP; solo recibe datos y manipula el DOM.
 *
 * Funciones que debes implementar aquí:
 *
 *   - renderizarListaMaterias(materias)
 *       Recibe el array de materias y construye el HTML
 *       para mostrarlas como tarjetas o ítems de lista.
 *       Cada ítem debe mostrar: nombre, código, color como muestra visual,
 *       sus bloques asignados (día y horario), y un botón "Eliminar".
 *
 *   - renderizarAlertasConflicto(conflictos)
 *       Recibe los conflictos detectados y muestra un mensaje claro
 *       indicando qué materias se cruzan y en qué día/horario.
 *       Si no hay conflictos, no muestra nada (o un mensaje de "Sin conflictos").
 *
 *   - limpiarLista()
 *       Vacía el contenedor de materias para poder redibujar desde cero.
 *
 * main.js es quien llama a estas funciones con los datos ya cargados.
 */
