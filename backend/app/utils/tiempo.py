"""
tiempo.py — Funciones auxiliares para trabajar con horas.

El sistema representa las horas como strings "HH:MM" en formato 24h.
Este archivo provee funciones para operar con ese formato de forma segura.

Funciones que debes implementar aquí:

  - hora_a_minutos(hora: str) -> int
      Convierte "08:30" a 510 (minutos desde medianoche).
      Trabajar con enteros es más simple y seguro que comparar strings.
      Ejemplo: "08:30" → 8*60 + 30 = 510
      Ejemplo: "13:00" → 13*60 + 0 = 780

  - minutos_a_hora(minutos: int) -> str
      Operación inversa. 510 → "08:30"

  - hora_valida(hora: str) -> bool
      Verifica que el string tenga formato correcto y represente una hora real.
      "25:00" → False  |  "abc" → False  |  "08:30" → True
      Útil para validar lo que el usuario ingresa antes de guardarlo.

Regla: funciones puras, sin efectos secundarios.
No importan nada del resto del proyecto. Se pueden probar de forma aislada.
"""
