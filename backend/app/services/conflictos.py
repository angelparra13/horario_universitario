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
