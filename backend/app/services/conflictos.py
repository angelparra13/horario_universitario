"""
conflictos.py — Algoritmo de detección de solapamiento entre bloques.

Separado de horario_service.py porque es la lógica más delicada
y debe ser fácil de probar de forma aislada.

Funciones que debes implementar aquí:

  - bloques_se_solapan(bloque_a, bloque_b) -> bool
      Recibe dos bloques y devuelve True si se cruzan en día y hora.
      Pasos sugeridos:
        1. Si los días son distintos, retornar False de inmediato.
        2. Convertir hora_inicio y hora_fin de ambos a minutos (usar utils/tiempo.py).
        3. Aplicar la lógica de solapamiento de intervalos:
           Dos rangos [a_ini, a_fin] y [b_ini, b_fin] se solapan si:
           a_ini < b_fin AND b_ini < a_fin
      Nota: debes decidir si el caso a_fin == b_ini cuenta como conflicto.

  - detectar_conflictos(lista_bloques) -> list
      Compara todos los bloques entre sí (cada par, sin repetir)
      y devuelve los pares que se solapan con información de qué materias afecta.

Regla: funciones puras. No leen ni escriben archivos. Solo reciben datos
y devuelven un resultado. Eso las hace fáciles de probar.
"""

from app.models import Bloque, Materia
from app.utils.tiempo import hora_a_minutos


def bloques_se_solapan(bloque_a: Bloque, bloque_b: Bloque) -> bool:
    # Paso 1: Verificar si los días son distintos
    if bloque_a.dia != bloque_b.dia:
        return False

    # Paso 2: Convertir horas a minutos
    a_inicio = hora_a_minutos(bloque_a.hora_inicio)
    a_fin = hora_a_minutos(bloque_a.hora_fin)
    b_inicio = hora_a_minutos(bloque_b.hora_inicio)
    b_fin = hora_a_minutos(bloque_b.hora_fin)

    # Paso 3: Verificar solapamiento de intervalos
    return a_inicio < b_fin and b_inicio < a_fin


def detectar_conflictos(lista_bloques: list[Bloque]) -> list[tuple[Bloque, Bloque]]:
    conflictos = []
    n = len(lista_bloques)

    # Comparar cada par de bloques sin repetir
    for i in range(n):
        for j in range(i + 1, n):
            bloque_a = lista_bloques[i]
            bloque_b = lista_bloques[j]
            if bloques_se_solapan(bloque_a, bloque_b):
                conflictos.append((bloque_a, bloque_b))
    return conflictos
