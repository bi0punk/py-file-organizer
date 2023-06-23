import os

def mostrar_directorios_principales():
    # Obtener la ruta del directorio principal del usuario
    ruta_usuario = os.path.expanduser("~")

    # Definir los nombres de los directorios principales
    nombres_directorios = ["Documentos", "Imágenes", "Música", "Vídeos"]

    # Mostrar los directorios principales del usuario
    for nombre in nombres_directorios:
        ruta_directorio = os.path.join(ruta_usuario, nombre)
        if os.path.isdir(ruta_directorio):
            print(f"Directorio {nombre}: {ruta_directorio}")

# Llamar a la función para mostrar los directorios principales del usuario
mostrar_directorios_principales()
