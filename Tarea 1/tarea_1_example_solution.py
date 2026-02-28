"""
Archivo que contiene las funciones solicitadas para la Tarea 1.
Curso: MT-7003 Microprocesadores y Microcontroladores

Descripción:
Este archivo implementa dos funciones principales:

1. filtrar_vocales:
   - Permite extraer vocales o consonantes de una cadena.
   - Incluye validaciones estrictas de entrada.
   - Devuelve códigos de error negativos según especificación.

2. encontrar_extremos:
   - Determina el valor mínimo y máximo de una lista numérica.
   - Valida tipo de dato, tamaño y contenido de la lista.
"""


def filtrar_vocales(cadena, bandera):
    """
    Filtra vocales o consonantes de una cadena según el valor de la bandera.

    Parámetros:
        cadena (str): Texto a procesar.
        bandera (bool):
            True  -> Retorna solo vocales.
            False -> Retorna solo consonantes.

    Retorna:
        tuple: (codigo_estado, resultado)
            codigo_estado = 0 si es exitoso.
            codigo_estado < 0 si ocurre error.
    """

    # Validación 1: cadena debe ser tipo string
    if not isinstance(cadena, str):
        return -100, None

    # Validación 2: cadena no puede ser vacía
    if cadena == "":
        return -300, None

    # Validación 3: cadena debe contener solo letras
    if not cadena.isalpha():
        return -200, None

    # Validación 4: máximo 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # Validación 5: bandera debe ser tipo booleano
    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"

    # Procesamiento principal
    if bandera:
        resultado = "".join(letra for letra in cadena if letra in vocales)
    else:
        resultado = "".join(letra for letra in cadena if letra not in vocales)

    return 0, resultado


def encontrar_extremos(lista):
    """
    Encuentra el valor mínimo y máximo de una lista numérica.

    Parámetros:
        lista (list): Lista de números (int o float).

    Retorna:
        tuple: (codigo_estado, minimo, maximo)
            codigo_estado = 0 si es exitoso.
            codigo_estado < 0 si ocurre error.
    """

    # Validación 1: debe ser lista
    if not isinstance(lista, list):
        return -600, None, None

    # Validación 2: lista no puede estar vacía
    if len(lista) == 0:
        return -800, None, None

    # Validación 3: máximo 15 elementos
    if len(lista) > 15:
        return -900, None, None

    # Validación 4: todos los elementos deben ser numéricos
    # (bool no es permitido aunque sea subtipo de int)
    for elemento in lista:
        if not isinstance(elemento, (int, float)) or isinstance(elemento, bool):
            return -700, None, None

    # Cálculo de extremos
    minimo = min(lista)
    maximo = max(lista)

    return 0, minimo, maximo