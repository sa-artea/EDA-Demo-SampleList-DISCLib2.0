﻿"""
Módulo con variables globales y funciones de comparación por defecto para uso por todo *DISClib* y sus ADTs.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


# python native modules
# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the node
from typing import TypeVar

# custom modules
# hash table entry class for the default cmp function

# valid data types for the node
# :data: VALID_DATA_TYPE_LT
VALID_DATA_TYPE_LT: tuple = (
    int,
    float,
    str,
    bool,
    dict,
    list,
    tuple,
    set,
    dataclass,
)
"""
Tupla con los tipos de datos nativos en Python que son comparables en los ADTs.
"""

# default key for comparing dictionaries
# :data: DEFAULT_DICT_KEY
DEFAULT_DICT_KEY: str = "id"
"""
Llave por defecto para comparar diccionarios dentro de los ADTs.
"""

# allowed input/output types for the ADTs
# :data: VALID_IO_TYPE
VALID_IO_TYPE: tuple = (
    list,
    tuple,
    set,
)
"""
Tupla con los tipos de datos nativos en Python que son válidos para entrada y salida de datos al inicializar un ADT.
"""

# default big prime number for MAD compression in hash tables
# :data: DEFAULT_PRIME
DEFAULT_PRIME: int = 109345121
"""
Número primo grande por defecto para la función de compresión MAD en las tablas de Hash.
"""


# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")
"""
Variable nativa de Python para definir una estructura de datos genérica en los ADTs.
"""


def lt_default_cmp_funcion(key, elm1, elm2) -> int:
    """*lt_default_cmp_funcion()* función de comparación por defecto para los elementos del ADT List (ArrayList, SingleLinked, DoubleLinked). pueden ser de tipo nativo o definido por el usuario.

    Args:
        key (str): llave para comparar los elementos de tipo diccionario.
        elm1 (any): primer elemento a comparar.
        elm2 (any): segundo elemento a comparar.

    Raises:
        TypeError: error de tipo de dato si los elementos de tipo nativo en Python no son comparables.
        KeyError: error de clave si la llave para comparar los diccionarios no existe.
        TypeError: error de tipo de dato si los elementos no son comparables.

    Returns:
        int: retorna -1 si elm1 es menor que elm2, 0 si son iguales y 1 si elm1 es mayor que elm2.
    """
    # TODO can be improved
    elm1_type = isinstance(elm1, VALID_DATA_TYPE_LT)
    elm2_type = isinstance(elm2, VALID_DATA_TYPE_LT)
    # if the elements are from different types, raise an exception
    if type(elm1) is not type(elm2):
        err_msg = f"Invalid comparison between {type(elm1)} and "
        err_msg += f"{type(elm2)} elements"
        raise TypeError(err_msg)
    # if there is a defined key
    elif key is not None:
        # if elements are dictionaries, compare their main key
        if isinstance(elm1, dict) and isinstance(elm2, dict):
            key1 = elm1.get(DEFAULT_DICT_KEY)
            key2 = elm2.get(DEFAULT_DICT_KEY)
            if None in [key1, key2]:
                err_msg = f"Invalid key: {DEFAULT_DICT_KEY}, "
                err_msg += "Key not found in one or both elements"
                raise KeyError(err_msg)
            # comparing elements
            else:
                # if one is less than the other, return -1
                if key1 < key2:
                    return -1
                # if they are equal, return 0
                elif key1 == key2:
                    return 0
                # if one is greater than the other, return 1
                elif key1 > key2:
                    return 1
                # otherwise, raise an exception
                else:
                    err_msg = f"Invalid comparison between {key1} and "
                    err_msg += f"{key2} keys in elements."
                    raise TypeError(err_msg)
        # if elements are native types, compare them directly
        elif elm1_type and elm2_type:
            # if one is less than the other, return -1
            if elm1 < elm2:
                return -1
            # if one is greater than the other, return 1
            elif elm1 > elm2:
                return 1
            # otherwise, they are equal, return 0
            else:
                return 0


def ht_default_cmp_funcion(key1, entry2) -> int:
    """*ht_default_cmp_funcion()* función de comparación por defecto para los elementos del ADT Map (HashTable). pueden ser de tipo nativo o definido por el usuario.

    Args:
        key1 (any): llave (key) para comparar del primer elemento (pareja llave-valor), el cual siempre es un MapEntry.
        entry2 (any): segundo elemento (pareja llave-valor) a comparar de tipo MapEntry. puede contener cualquier tipo de dato.

    Returns:
        int: retorna -1 si key1 es menor que la llave de entry2, 0 si las llaves son iguales y 1 si key1 es mayor que la llave de entry2.
    """
    key2 = entry2.get_key()
    if type(key1) is not type(key2):
        err_msg = f"Invalid comparison between {type(key1)} and "
        err_msg += f"{type(key2)} keys"
        raise TypeError(err_msg)
    if (key1 == key2):
        return 0
    elif (key1 > key2):
        return 1
    return -1
