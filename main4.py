import os

def listar_directorios_principales(ruta):
    directorios_principales = []
    for elemento in os.listdir(ruta):
        ruta_elemento = os.path.join(ruta, elemento)
        if os.path.isdir(ruta_elemento) and not elemento.startswith('.'):
            directorios_principales.append(elemento)
    return directorios_principales

ruta_base = os.path.expanduser("~")
print("Ruta base:", ruta_base)

directorios_principales = listar_directorios_principales(ruta_base)

for directorio in directorios_principales:
    print(directorio)
