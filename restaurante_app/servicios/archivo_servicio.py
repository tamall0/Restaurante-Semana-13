import json
import os
from typing import List, TypeVar, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario

T = TypeVar('T')

class ArchivoServicio:
    def __init__(self, ruta_productos: str = "datos/productos.json", ruta_usuarios: str = "datos/usuarios.json"):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios

    def _cargar_coleccion(self, ruta: str, transformador: Callable[[dict], T]) -> List[T]:
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if not isinstance(datos, list):
                    return []
                return [transformador(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, PermissionError):
            return []

    def cargar_productos(self) -> List[Producto]:
        return self._cargar_coleccion(self.ruta_productos, Producto.desde_diccionario)

    def cargar_usuarios(self) -> List[Usuario]:
        return self._cargar_coleccion(self.ruta_usuarios, Usuario.desde_diccionario)