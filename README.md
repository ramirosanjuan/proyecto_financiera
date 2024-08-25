# Administrador de Tareas

Este proyecto es una aplicación de escritorio para la gestión de tareas y transacciones financieras. La aplicación permite a los usuarios agregar, modificar y eliminar transacciones, así como ver reportes y paneles de control.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- `modelo.py`: Define las clases de datos para las transacciones.
- `vista.py`: Define la interfaz gráfica de usuario (GUI) principal utilizando Tkinter.
- `vista_main.py`: Define los widgets para la vista principal de la aplicación.
- `vista_panel_control.py`: Define los widgets para el panel de control.
- `vista_reportes.py`: Define los widgets para la vista de reportes.
- `vista_transacciones.py`: Define los widgets para la vista de transacciones.
- `controlador.py`: Punto de entrada principal de la aplicación.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual y activa el entorno:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    # source venv/bin/activate  # En macOS/Linux
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    python controlador.py
    ```

2. La aplicación se abrirá con una ventana principal que contiene varias pestañas:
    - **Main**: Permite agregar nuevas transacciones.
    - **Panel de control**: Muestra un panel de control (aún por implementar).
    - **Transacciones**: Muestra las transacciones registradas (aún por implementar).
    - **Reportes**: Muestra reportes financieros (aún por implementar).
