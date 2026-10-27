# Proyecto Blog

Sistema de gestión de posts en consola desarrollado en Python con persistencia de datos en JSON.

# Estructura

`main.py`:  entrada principal.
 `posts.json`: Archivo donde se guardan las publicaciones.
 `blog/`:
   `datos.py`: Carga y guardado de datos en JSON.
   `modelos.py`: Clases del sistema (`Autor`, `Post`, `Blog`).
   `menu.py`: Menú interactivo de consola.
   `operaciones.py`: Funciones de búsqueda y filtrado.
   `validaciones.py`: Validaciones de entrada.

# Cómo ejecutarlo

 estar en la carpeta de  `proyecto_blog` y ejecutar:

```bash
python main.py