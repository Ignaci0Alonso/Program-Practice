import os
import sys

try:
    ruta = sys.argv[1]
    extencion = sys.argv[2]
except IndexError:
    print("Argumentos insuficientes.")
    sys.exit()

try:
    archivos = os.listdir(ruta)
except FileNotFoundError:
    print("La ruta no existe.")

if not extencion.startswith("."):
    extencion = "." + extencion

for archivo in archivos:
    print(archivo)

# archivos = os.listdir("C:\\Temporal")
# confirm = False

# try:
#     for archivo in archivos:
#         if archivo.endswith("exe"):
#             print(archivo)
#             confirm = True
#     if confirm == False:
#         print("Argumentos insuficientes")
# except FileNotFoundError:
#     print("""Error de sistema.
#     El directorio seleccionado no existe.""")
#     sys.exit()