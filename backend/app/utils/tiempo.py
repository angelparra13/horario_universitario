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

def hora_a_minutos(hora: str) -> int:
    """Convierte una hora en formato "HH:MM" a minutos desde medianoche."""
    if not hora_valida(hora):
        raise ValueError(f"Hora inválida: {hora}")
    horas, minutos = map(int, hora.split(":"))
    return horas * 60 + minutos

def minutos_a_hora(minutos: int) -> str:
    """Convierte minutos desde medianoche a formato "HH:MM"."""
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return f"{horas:02d}:{minutos_restantes:02d}"

def hora_valida(hora: str) -> bool:
    """Verifica que el string tenga formato correcto y represente una hora real."""
    if not isinstance(hora, str):
        return False
    partes = hora.split(":")
    if len(partes) != 2:
        return False
    try:
        horas = int(partes[0])
        minutos = int(partes[1])
        return 0 <= horas < 24 and 0 <= minutos < 60
    except ValueError:
        return False
