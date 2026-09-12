# Restaurante App - Semana 13

Primera versión con interfaz gráfica de usuario (**GUI**) desarrollada en **Tkinter** para la gestión básica de productos y usuarios en `restaurante_app`.

## Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Flujo de la Aplicación

1. **Inicio**: `main.py` inicializa la ventana Tkinter y carga las colecciones desde los archivos JSON mediante `ArchivoServicio` y `RestauranteServicio`.
2. **Acceso**: Se presenta la pantalla `LoginView`. Se verifica la combinación de usuario y clave.
3. **Panel Principal**: Tras una autenticación exitosa, la aplicación intercambia la vista a `MainView` sin abrir nuevas ventanas.
4. **Consulta**: Se listan los productos y usuarios cargados desde la capa de servicios.
5. **Cierre de Sesión**: Regresa a la vista `LoginView`.

## Instrucciones de Ejecución

Asegúrese de ejecutar el script desde el directorio raíz del proyecto:

```bash
python main.py
```
**ID de Usuario:**

admin

**Contraseña:**

1234
