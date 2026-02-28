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

    # Verificar que cadena sea string
    if not isinstance(cadena, str):
        return FV_ERROR_NO_STRING, None

    # Verificar que cadena no sea vacía
    if cadena == "":
        return FV_ERROR_CADENA_VACIA, None

    # Verificar longitud máxima
    if len(cadena) > 30:
        return FV_ERROR_LONGITUD_EXCEDIDA, None

    # Verificar que solo contenga letras
    if not cadena.isalpha():
        return FV_ERROR_NO_SOLO_LETRAS, None

    # Verificar que bandera sea booleano
    if not isinstance(bandera, bool):
        return FV_ERROR_BANDERA_NO_BOOL, None

    vocales = "aeiouAEIOU"

    if bandera:
        resultado = "".join(c for c in cadena if c in vocales)
    else:
        resultado = "".join(c for c in cadena if c not in vocales)

    return FV_OK, resultado


# ==============================
# FUNCIÓN 2: encontrar_extremos
# ==============================

def encontrar_extremos(lista_numeros):

    # Verificar que sea lista
    if not isinstance(lista_numeros, list):
        return EE_ERROR_NO_LISTA, None, None

    # Verificar que no esté vacía
    if len(lista_numeros) == 0:
        return EE_ERROR_LISTA_VACIA, None, None

    # Verificar longitud máxima
    if len(lista_numeros) > 15:
        return EE_ERROR_LONGITUD_EXCEDIDA, None, None

    # Verificar que todos sean números (pero NO aceptar bool)
    for elemento in lista_numeros:
        if not (type(elemento) == int or type(elemento) == float):
            return EE_ERROR_ELEMENTOS_NO_NUMERICOS, None, None

    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return EE_OK, minimo, maximo