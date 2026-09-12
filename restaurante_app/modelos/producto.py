class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str, stock: int = 0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @property
    def id_producto(self) -> int:
        return self._id_producto

    @id_producto.setter
    def id_producto(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del producto debe ser un entero positivo.")
        self._id_producto = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")
        self._precio = float(valor)

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def a_diccionario(self) -> dict:
        return {
            "id_producto": self._id_producto,
            "nombre": self._nombre,
            "precio": self._precio,
            "categoria": self._categoria,
            "stock": self._stock
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            id_producto=datos["id_producto"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            categoria=datos["categoria"],
            stock=datos.get("stock", 0)
        )

    def __str__(self) -> str:
        return f"[{self._id_producto}] {self._nombre} - ${self._precio:.2f} ({self._categoria}) | Stock: {self._stock}"