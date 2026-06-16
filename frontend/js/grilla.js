/*
 * grilla.js — Construcción y renderizado de la grilla visual semanal
 *
 * Este es el archivo más complejo del frontend.
 * Su única responsabilidad es tomar los datos de materias y bloques
 * y construir la representación visual en el DOM de horario.html.
 *
 * Funciones que debes implementar aquí:
 *
 *   - construirGrilla(contenedor)
 *       Crea la estructura HTML base de la grilla:
 *       encabezados de días (Lun, Mar, Mié...), columna de horas,
 *       y las celdas vacías del fondo.
 *
 *   - renderizarBloques(bloques, materias)
 *       Recibe la lista de bloques y materias, y coloca cada bloque
 *       en su posición correcta dentro de la grilla.
 *       - Columna = día de la semana
 *       - Fila / posición vertical = hora de inicio
 *       - Altura = proporcional a la duración del bloque
 *       - Color de fondo = color de la materia correspondiente
 *
 *   - marcarConflictos(conflictos)
 *       Recibe los pares en conflicto y añade una clase CSS especial
 *       a los bloques afectados para resaltarlos visualmente (ej. borde rojo).
 *
 *   - limpiarGrilla()
 *       Elimina los bloques renderizados sin destruir la estructura base.
 *       Útil para redibujar cuando cambian los datos.
 *
 * Este archivo no hace peticiones HTTP.
 * Recibe datos ya cargados y solo manipula el DOM.
 */
