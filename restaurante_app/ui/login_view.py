import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable

class LoginView(ttk.Frame):
    def __init__(self, parent: tk.Widget, restaurante_servicio, on_login_success: Callable[[], None]):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login_success = on_login_success

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        card = ttk.Frame(self, padding=30, relief="groove")
        card.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(card, text="Acceso al Sistema", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(card, text="ID Usuario:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_usuario = ttk.Entry(card, width=25)
        self.txt_usuario.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(card, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_clave = ttk.Entry(card, width=25, show="*")
        self.txt_clave.grid(row=2, column=1, pady=5, padx=5)

        btn_ingresar = ttk.Button(card, text="Iniciar Sesión", command=self._procesar_login)
        btn_ingresar.grid(row=3, column=0, columnspan=2, pady=(15, 0))

    def _procesar_login(self) -> None:
        usr = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if not usr or not clave:
            messagebox.showwarning("Atención", "Por favor ingrese usuario y contraseña.")
            return

        if self.restaurante_servicio.validar_acceso(usr, clave):
            self.txt_usuario.delete(0, tk.END)
            self.txt_clave.delete(0, tk.END)
            self.on_login_success()
        else:
            messagebox.showerror("Error de Acceso", "Credenciales incorrectas. Intente nuevamente.")