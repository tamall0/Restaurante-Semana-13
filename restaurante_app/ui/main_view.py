import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable

class MainView(ttk.Frame):
    def __init__(self, parent: tk.Widget, restaurante_servicio, on_logout: Callable[[], None]):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        # Encabezado
        header = ttk.Frame(self, padding=10)
        header.pack(fill="x")

        ttk.Label(header, text="Panel Principal - Restaurante App", font=("Helvetica", 14, "bold")).pack(side="left")
        ttk.Button(header, text="Cerrar Sesión", command=self.on_logout).pack(side="right")

        # Pestañas del Sistema
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Productos
        self.tab_productos = ttk.Frame(notebook, padding=10)
        notebook.add(self.tab_productos, text="Productos")
        self._construir_pestana_productos()

        # Pestaña 2: Usuarios
        self.tab_usuarios = ttk.Frame(notebook, padding=10)
        notebook.add(self.tab_usuarios, text="Usuarios")
        self._construir_pestana_usuarios()

        # Pestaña 3: Ventas (Funcionalidad pendiente)
        tab_ventas = ttk.Frame(notebook, padding=10)
        notebook.add(tab_ventas, text="Ventas")
        ttk.Label(tab_ventas, text="Módulo de Ventas en desarrollo (Pendiente para próximas semanas)", font=("Helvetica", 11, "italic")).pack(pady=40)

    def _construir_pestana_productos(self) -> None:
        lbl_info = ttk.Label(self.tab_productos, text="", font=("Helvetica", 10, "bold"))
        lbl_info.pack(anchor="w", pady=(0, 5))

        listbox = tk.Listbox(self.tab_productos, font=("Consolas", 10))
        listbox.pack(fill="both", expand=True)

        productos = self.restaurante_servicio.obtener_productos()
        lbl_info.config(text=f"Total Productos Registrados: {len(productos)}")

        for p in productos:
            listbox.insert(tk.END, str(p))

    def _construir_pestana_usuarios(self) -> None:
        lbl_info = ttk.Label(self.tab_usuarios, text="", font=("Helvetica", 10, "bold"))
        lbl_info.pack(anchor="w", pady=(0, 5))

        listbox = tk.Listbox(self.tab_usuarios, font=("Consolas", 10))
        listbox.pack(fill="both", expand=True)

        usuarios = self.restaurante_servicio.obtener_usuarios()
        lbl_info.config(text=f"Total Usuarios Registrados: {len(usuarios)}")

        for u in usuarios:
            listbox.insert(tk.END, str(u))

    def refrescar_datos(self) -> None:
        """Permite actualizar las vistas si cambian las colecciones subyacentes."""
        for widget in self.tab_productos.winfo_children():
            widget.destroy()
        for widget in self.tab_usuarios.winfo_children():
            widget.destroy()

        self._construir_pestana_productos()
        self._construir_pestana_usuarios()