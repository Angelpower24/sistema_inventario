"""
Modulo de Modelos - Producto
Define las entidades principales del sistema
"""
from datetime import datetime
from enum import Enum

class Categoria(Enum):
    """Enumeracion de categorias de productos."""
    ELECTRONICA = "Electronica"
    ALIMENTOS = "Alimentos"
    ROPA = "Ropa"
    LIBROS = "Libros"
    OTROS = "Otros"
