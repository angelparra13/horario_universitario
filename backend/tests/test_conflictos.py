"""
test_conflictos.py — Pruebas para el algoritmo de detección de conflictos.

Este es el archivo de pruebas más importante porque el algoritmo
de solapamiento tiene varios casos borde no obvios.

Casos que DEBES probar (de menor a mayor complejidad):
  1. Dos bloques en días distintos                       → no hay conflicto
  2. Dos bloques el mismo día que no se tocan            → no hay conflicto
  3. Un bloque termina exactamente cuando el otro empieza → decidir (¿conflicto?)
  4. Dos bloques que se solapan parcialmente             → conflicto
  5. Un bloque completamente dentro del otro             → conflicto
  6. Dos bloques con exactamente el mismo horario        → conflicto
  7. Lista de 3 bloques donde solo 2 se cruzan           → devuelve solo ese par
  8. Lista de 4 bloques sin ningún conflicto             → devuelve lista vacía

Cómo correr las pruebas:
  pytest tests/test_conflictos.py

Consejo: prueba bloques_se_solapan() de forma aislada antes de
probar detectar_conflictos(). Es más fácil encontrar errores así.
"""
