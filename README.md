# QR Code Generator GUI

Este proyecto es una aplicación gráfica para generar códigos QR de manera sencilla e intuitiva. Permite a los usuarios ingresar una URL, seleccionar un color y cargar un logo para personalizar el código QR generado.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
qr-generator-gui
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── gui.py           # Interfaz gráfica de usuario
│   └── utils
│       └── qr_utils.py  # Funciones auxiliares para generar códigos QR
├── requirements.txt      # Dependencias del proyecto
├── setup.py              # Script de configuración para la instalación
└── README.md             # Documentación del proyecto
```

## Instalación

1. Clona el repositorio en tu máquina local:

```sh
   git clone https://github.com/tu-usuario/qr-generator-gui.git
   cd qr-generator-gui
```

2. Crea un entorno virtual utilizando venv:

```sh
python3 -m venv venv
```
3. Activa el entorno virtual
    - En macOS y Linux:
    ```sh
    source venv/bin/activate
    ```
    - En Windows:
    ```sh
    .\venv\Scripts\activate
    ```

4. Instala las dependencias necesarias:
```sh
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación utilizando el siguiente comando:

   ```sh
   python src.main.py
   ```

2. La interfaz gráfica se abrirá, permitiéndote ingresar la URL, seleccionar el color de un selector de colores que cargará el valor en hexadecimal o puede introducirse de forma manual y un cargar una imagen que irá en el centro del código QR (opcional).

3. Haz clic en el botón para generar el código QR. El código QR se mostrará en la interfaz y podrás copiarlo al portapapeles o guardarlo como una imagen.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.