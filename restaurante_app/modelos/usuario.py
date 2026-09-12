class Usuario:
    def __init__(self, id_usuario: str, nombre: str, rol: str, clave: str = "1234"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol
        self.clave = clave

    @property
    def id_usuario(self) -> str:
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El ID de usuario no puede estar vacío.")
        self._id_usuario = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El rol no puede estar vacío.")
        self._rol = valor.strip()

    @property
    def clave(self) -> str:
        return self._clave

    @clave.setter
    def clave(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La clave no puede estar vacía.")
        self._clave = valor.strip()

    def a_diccionario(self) -> dict:
        return {
            "id_usuario": self._id_usuario,
            "nombre": self._nombre,
            "rol": self._rol,
            "clave": self._clave
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        return cls(
            id_usuario=str(datos["id_usuario"]),
            nombre=datos["nombre"],
            rol=datos["rol"],
            clave=datos.get("clave", "1234")
        )

    def __str__(self) -> str:
        return f"[{self._id_usuario}] {self._nombre} - Rol: {self._rol}"