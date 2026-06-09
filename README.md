Guía de errores y ejecución:
Requisitos previos:

Python 3.12 instalado
El archivo gotaagua.jpg debe estar en la misma carpeta que los scripts

Cómo correrlo:
Abre una terminal en la carpeta del proyecto y ejecuta:
py -3.12 "Gotita De AGua.py"
py -3.12 lluvia.py

Si aparece ModuleNotFoundError: No module named 'pygame':
py -3.12 -m pip install pygame
Luego vuelve a correr el script. Asegúrate de usar siempre py -3.12 y no otra versión de Python, o pygame no será encontrado.

Si aparece No runtime installed that matches 3.12:
py install 3.12
Después instala pygame y corre el script normalmente.

Si la imagen no carga (FileNotFoundError):
Verifica que gotaagua.jpg esté en la misma carpeta que el .py. Los scripts buscan la imagen automáticamente en su propia carpeta, así que no muevas uno sin el otro.
