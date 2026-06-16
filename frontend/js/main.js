/*
 * main.js — Inicialización y coordinación de index.html
 *
 * Este es el punto de entrada del JavaScript en index.html.
 * Su responsabilidad es conectar todas las piezas:
 *
 *   Al cargar la página:
 *     - Pedir la lista de materias al backend (api.js)
 *     - Renderizarlas en pantalla (materias.js)
 *     - Consultar conflictos y mostrar alertas si hay (materias.js)
 *
 *   Al enviar el formulario de materia:
 *     - Llamar a crearMateria() de api.js
 *     - Refrescar la lista en pantalla
 *
 *   Al enviar el formulario de bloque:
 *     - Llamar a crearBloque() de api.js
 *     - Refrescar la lista en pantalla
 *     - Volver a consultar conflictos
 *
 *   Al hacer clic en "eliminar" una materia:
 *     - Llamar a eliminarMateria() de api.js
 *     - Refrescar la lista en pantalla
 *
 * Regla: este archivo orquesta, no implementa lógica propia.
 * El renderizado va en materias.js. Las peticiones HTTP van en api.js.
 * main.js solo conecta eventos del DOM con funciones de esos archivos.
 */
