import os
import shutil

# Directorio a organizar
disorder_directory_files = "/you/route"

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
            
            # Ruta completa del archivo en el directorio de origen
            source_file_path = os.path.join(disorder_directory_files, file_name)
            # Ruta completa del archivo en el directorio de destino
            target_file_path = os.path.join(target_dir, file_name)
            
            # Verificar si el archivo ya existe en el directorio de destino
            if os.path.exists(target_file_path):
                print(f"El archivo '{file_name}' ya existe en el directorio de destino.")
            else:
                # Mover el archivo al directorio correspondiente
                shutil.move(source_file_path, target_file_path)
    except Exception as e:
        print(f"Error al organizar el archivo '{file_name}': {str(e)}")

print("Archivos organizados con éxito.")
