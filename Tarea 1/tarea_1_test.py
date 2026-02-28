import Tarea_1_Gabriel_y_Hillary
import random
import string
import pytest


# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo filtrar_vocales
# -100 cadena no es string
# -200 cadena tiene caracteres no alfabeticos
# -300 cadena vacia
# -400 cadena mayor a 30 caracteres
# -500 bandera no es booleano

# Errores esperados metodo encontrar_extremos
# -600 parametro no es lista
# -700 elementos no numericos
# -800 lista vacia
# -900 mas de 15 elementos


def test_casos_error_filtrar_vocales():

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena=123,
        bandera=True
    )
    assert estado == -100
    assert res is None

    random_string = "abc{}123".format(
        random.choice(string.punctuation)
    )
    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena=random_string,
        bandera=True
    )
    assert estado == -200
    assert res is None

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="",
        bandera=False
    )
    assert estado == -300
    assert res is None

    long_string = "a" * 31
    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena=long_string,
        bandera=True
    )
    assert estado == -400
    assert res is None

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="ejemplo",
        bandera="True"
    )
    assert estado == -500
    assert res is None

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="ejemplo",
        bandera=1
    )
    assert estado == -500
    assert res is None


def test_casos_exito_filtrar_vocales():

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="HolaMundo",
        bandera=True
    )
    assert estado == 0
    assert res == "oauo"

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="HolaMundo",
        bandera=False
    )
    assert estado == 0
    assert res == "HlMnd"

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="aeiou",
        bandera=True
    )
    assert estado == 0
    assert res == "aeiou"

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="bcdfg",
        bandera=True
    )
    assert estado == 0
    assert res == ""

    estado, res = Tarea_1_Gabriel_y_Hillary.filtrar_vocales(
        cadena="AEIOUaeiou",
        bandera=False
    )
    assert estado == 0
    assert res == ""


def test_casos_error_encontrar_extremos():

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            "no es lista"
        )
    )
    assert estado == -600
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            123
        )
    )
    assert estado == -600
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            [1, 2, "3", 4]
        )
    )
    assert estado == -700
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            [1, 2, True, 4]
        )
    )
    assert estado == -700
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            []
        )
    )
    assert estado == -800
    assert minimo is None
    assert maximo is None

    lista_larga = list(range(16))
    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_larga
        )
    )
    assert estado == -900
    assert minimo is None
    assert maximo is None


def test_casos_exito_encontrar_extremos():

    lista_prueba = [5, 2, 8, 1, 9, 3]
    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_prueba
        )
    )
    assert estado == 0
    assert minimo == 1
    assert maximo == 9

    lista_prueba = [-5, -2, -8, -1]
    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_prueba
        )
    )
    assert estado == 0
    assert minimo == -8
    assert maximo == -1

    lista_prueba = [3.5, 1.2, 9.8, 2.1]
    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_prueba
        )
    )
    assert estado == 0
    assert minimo == 1.2
    assert maximo == 9.8

    lista_prueba = [42]
    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_prueba
        )
    )
    assert estado == 0
    assert minimo == 42
    assert maximo == 42

    lista_prueba = [
        random.randint(-100, 100)
        for _ in range(random.randint(2, 15))
    ]
    esperado_min = min(lista_prueba)
    esperado_max = max(lista_prueba)

    estado, minimo, maximo = (
        Tarea_1_Gabriel_y_Hillary.encontrar_extremos(
            lista_prueba
        )
    )
    assert estado == 0
    assert minimo == esperado_min
    assert maximo == esperado_max
