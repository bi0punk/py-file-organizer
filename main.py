
#importamos librerias
import os

import shutil
from time import sleep
from progressbar import progressbar


# Directorio a organizar
disorder_directory_files = "/home/sysbot/Descargas/"

# Crear un diccionario vacío para almacenar los directorios
dirs = {}

# Recorrer todos los archivos en el directorio
for file_name in os.listdir(disorder_directory_files):
    # Obtener la extensión del archivo
    extension = os.path.splitext(file_name)[1]

    # Si la extensión no está en el diccionario, crear un nuevo directorio para ella
    if extension not in dirs:
        dirs[extension] = os.path.join(disorder_directory_files, extension[1:])
        os.makedirs(dirs[extension], exist_ok=True)

    # Mover el archivo al directorio correspondiente
    shutil.move(os.path.join(disorder_directory_files, file_name), 
                os.path.join(dirs[extension], file_name))


for i in progressbar(range(100)):
    sleep(0.02)
print("Archivos organizados con éxito.")
