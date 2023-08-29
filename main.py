import os
import shutil
# Directorio a organizar
disorder_directory_files = "you/route"
# Crear un diccionario vacío para almacenar los directorios
extension_dirs = {}
# Recorrer todos los archivos en el directorio
for file_name in os.listdir(disorder_directory_files):
    try:
        # Obtener la extensión del archivo
        extension = os.path.splitext(file_name)[1]
        # Si la extensión no está en el diccionario, crear un nuevo directorio para ella
        if extension:
            target_dir = os.path.join(disorder_directory_files, extension[1:])
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            # Mover el archivo al directorio correspondiente
            shutil.move(os.path.join(disorder_directory_files, file_name), 
                        os.path.join(target_dir, file_name))
    except Exception as e:
        print(f"Error al organizar el archivo '{file_name}': {str(e)}")

print("Archivos organizados con éxito.")
