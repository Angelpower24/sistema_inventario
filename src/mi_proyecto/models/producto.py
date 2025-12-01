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

class Producto:
    """
    Representa un producto en el inventario.

    Attributes:
        id_producto (int): Identificador unico
        nombre (str): Nombre del producto
        descripcion (str): Descripcion del producto
        precio (float): Precio unitario
        cantidad (int): Cantidad en stock
        categoria (Categoria): Categoria del producto
        fecha_creacion (str): Fecha de creacion
    """
    
    __contador = 1000