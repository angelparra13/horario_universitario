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

from app.models import Bloque
from app.services.conflictos import bloques_se_solapan, detectar_conflictos

def test_bloques_en_dias_distintos():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Martes", hora_inicio="08:00", hora_fin="10:00")
    assert not bloques_se_solapan(bloque_a, bloque_b)

def test_bloques_mismo_dia_no_se_tocan():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="10:00", hora_fin="12:00")
    assert not bloques_se_solapan(bloque_a, bloque_b)

def test_bloques_mismo_dia_termina_empieza():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="10:00", hora_fin="12:00")
    # Decidimos que esto NO es un conflicto porque no se solapan en ningún minuto
    assert not bloques_se_solapan(bloque_a, bloque_b)

def test_bloques_se_solapan_parcialmente():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="09:00", hora_fin="11:00")
    assert bloques_se_solapan(bloque_a, bloque_b)

def test_bloques_uno_dentro_del_otro():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="12:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="09:00", hora_fin="10:00")
    assert bloques_se_solapan(bloque_a, bloque_b)

def test_bloques_mismo_horario():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    assert bloques_se_solapan(bloque_a, bloque_b)

def test_detectar_conflictos_varios_bloques():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="09:00", hora_fin="11:00")
    bloque_c = Bloque(id=3, id_materia=3, dia="Martes", hora_inicio="08:00", hora_fin="10:00")
    bloque_d = Bloque(id=4, id_materia=4, dia="Lunes", hora_inicio="11:00", hora_fin="12:00")

    lista_bloques = [bloque_a, bloque_b, bloque_c, bloque_d]
    conflictos = detectar_conflictos(lista_bloques)

    # Solo bloque_a y bloque_b se solapan
    assert len(conflictos) == 1
    assert (bloque_a, bloque_b) in conflictos or (bloque_b, bloque_a) in conflictos

def test_detectar_conflictos_sin_conflictos():
    bloque_a = Bloque(id=1, id_materia=1, dia="Lunes", hora_inicio="08:00", hora_fin="10:00")
    bloque_b = Bloque(id=2, id_materia=2, dia="Lunes", hora_inicio="10:00", hora_fin="12:00")
    bloque_c = Bloque(id=3, id_materia=3, dia="Martes", hora_inicio="08:00", hora_fin="10:00")
    bloque_d = Bloque(id=4, id_materia=4, dia="Lunes", hora_inicio="12:00", hora_fin="13:00")

    lista_bloques = [bloque_a, bloque_b, bloque_c, bloque_d]
    conflictos = detectar_conflictos(lista_bloques)

    # No hay conflictos
    assert len(conflictos) == 0
