# Folder Organizer

Este script organiza los archivos en un directorio especificado, moviéndolos a subdirectorios basados en sus extensiones de archivo.

## Descripción

El script recorre todos los archivos en el directorio especificado (`disorder_directory_files`) y los mueve a subdirectorios nombrados según la extensión del archivo. Si el archivo ya existe en el subdirectorio de destino, el script lo notifica y no lo mueve. Al finalizar, muestra la cantidad de archivos organizados por cada extensión.

## Requisitos

- Python 3.x
- Módulos estándar de Python: `os`, `shutil`

## Uso

1. Clona este repositorio o descarga el script a tu máquina local.
2. Abre el script y modifica la variable `disorder_directory_files` para que apunte al directorio que deseas organizar.
3. Ejecuta el script con Python.

## Ejemplo de ejecución

```bash
python folder_organizer.py
