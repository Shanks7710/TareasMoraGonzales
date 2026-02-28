# ==========================================
# Tarea_1_Gabriel_y_Hillary.py
# ==========================================

# ==============================
# CÓDIGOS DE RETORNO
# ==============================

# filtrar_vocales
FV_OK = 0
FV_ERROR_NO_STRING = -100
FV_ERROR_NO_SOLO_LETRAS = -200
FV_ERROR_CADENA_VACIA = -300
FV_ERROR_LONGITUD_EXCEDIDA = -400
FV_ERROR_BANDERA_NO_BOOL = -500

# encontrar_extremos
EE_OK = 0
EE_ERROR_NO_LISTA = -600
EE_ERROR_ELEMENTOS_NO_NUMERICOS = -700
EE_ERROR_LISTA_VACIA = -800
EE_ERROR_LONGITUD_EXCEDIDA = -900


# ==============================
# FUNCIÓN 1: filtrar_vocales
# ==============================

def filtrar_vocales(cadena, bandera):
    """
    Filtra vocales o consonantes de una cadena según el valor
    de la bandera.

    Parámetros:
        cadena (str): Texto a analizar. Debe contener solo letras
                      y tener máximo 30 caracteres.
        bandera (bool): Si es True retorna solo vocales.
                        Si es False retorna solo consonantes.

    Retorna:
        (int, str | None):
            Código de estado y el string filtrado.
            En caso de error retorna (código_error, None).
    """

    # Validar que cadena sea tipo string
    if not isinstance(cadena, str):
        return FV_ERROR_NO_STRING, None

    # Validar que no sea cadena vacía
    if cadena == "":
        return FV_ERROR_CADENA_VACIA, None

    # Validar longitud máxima permitida
    if len(cadena) > 30:
        return FV_ERROR_LONGITUD_EXCEDIDA, None

    # Validar que solo contenga letras del abecedario
    if not cadena.isalpha():
        return FV_ERROR_NO_SOLO_LETRAS, None

    # Validar que bandera sea booleano
    if not isinstance(bandera, bool):
        return FV_ERROR_BANDERA_NO_BOOL, None

    # Conjunto de vocales permitidas
    vocales = "aeiouAEIOU"

    # Filtrado según el valor de bandera
    if bandera:
        resultado = "".join(
            caracter for caracter in cadena
            if caracter in vocales
        )
    else:
        resultado = "".join(
            caracter for caracter in cadena
            if caracter not in vocales
        )

    return FV_OK, resultado


# ==============================
# FUNCIÓN 2: encontrar_extremos
# ==============================

def encontrar_extremos(lista_numeros):
    """
    Determina el valor mínimo y máximo de una lista numérica.

    Parámetros:
        lista_numeros (list): Lista con números enteros o
                              flotantes. Máximo 15 elementos.

    Retorna:
        (int, int|float|None, int|float|None):
            Código de estado, valor mínimo y valor máximo.
            En caso de error retorna (código_error, None, None).
    """

    # Validar que el parámetro sea una lista
    if not isinstance(lista_numeros, list):
        return EE_ERROR_NO_LISTA, None, None

    # Validar que la lista no esté vacía
    if len(lista_numeros) == 0:
        return EE_ERROR_LISTA_VACIA, None, None

    # Validar que no exceda 15 elementos
    if len(lista_numeros) > 15:
        return EE_ERROR_LONGITUD_EXCEDIDA, None, None

    # Validar que todos los elementos sean int o float
    # Se usa type(...) is para excluir bool explícitamente
    for elemento in lista_numeros:
        if type(elemento) is not int and type(elemento) is not float:
            return EE_ERROR_ELEMENTOS_NO_NUMERICOS, None, None

    # Calcular valores extremos
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return EE_OK, minimo, maximo
