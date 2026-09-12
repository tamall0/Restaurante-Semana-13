import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AppController:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("650x450")
        self.root.minsize(500, 350)

        # Instanciación de servicios
        archivo_servicio = ArchivoServicio()
        self.restaurante_servicio = RestauranteServicio(archivo_servicio)

        # Contenedor principal de vistas
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Inicialización de las vistas
        self.login_view = LoginView(self.container, self.restaurante_servicio, self.mostrar_main)
        self.main_view = MainView(self.container, self.restaurante_servicio, self.mostrar_login)

        # Vista inicial
        self.mostrar_login()

    def mostrar_login(self) -> None:
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main(self) -> None:
        self.login_view.pack_forget()
        self.main_view.refrescar_datos()
        self.main_view.pack(fill="both", expand=True)

def main():
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()