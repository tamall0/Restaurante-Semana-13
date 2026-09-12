from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, archivo_servicio: ArchivoServicio):
        self._archivo_servicio = archivo_servicio
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self) -> None:
        self._productos = self._archivo_servicio.cargar_productos()
        self._usuarios = self._archivo_servicio.cargar_usuarios()

        # Garantiza que siempre exista al menos un usuario para poder probar la GUI
        if not self._usuarios:
            admin_defecto = Usuario(
                id_usuario="admin",
                nombre="Administrador",
                rol="Administrador",
                clave="1234"
            )
            self._usuarios.append(admin_defecto)

    def validar_acceso(self, id_usuario: str, clave: str) -> bool:
        """Valida si el usuario y la clave ingresados coinciden."""
        id_limpio = id_usuario.strip()
        clave_limpia = clave.strip()

        for u in self._usuarios:
            if u.id_usuario == id_limpio and u.clave == clave_limpia:
                return True
        return False

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios

    def obtener_cantidad_productos(self) -> int:
        return len(self._productos)

    def obtener_cantidad_usuarios(self) -> int:
        return len(self._usuarios)