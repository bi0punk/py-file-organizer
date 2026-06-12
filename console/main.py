import os
import shutil
from collections import defaultdict
from pathlib import Path


def organizar_por_extension(
    base_dir: str = ".",
    verbose: bool = True,
) -> dict[str, int]:

    base_path = Path(base_dir).expanduser().resolve()

    if not base_path.exists():
        raise FileNotFoundError(f"El directorio '{base_path}' no existe.")

    if not base_path.is_dir():
        raise NotADirectoryError(f"'{base_path}' no es un directorio.")

    extension_dirs: dict[str, int] = defaultdict(int)

    # Usamos scandir para más rendimiento que listdir
    with os.scandir(base_path) as it:
        for entry in it:
            file_name = entry.name

            # Saltar directorios; solo trabajamos con archivos
            if not entry.is_file():
                continue

            try:
                # Obtener la extensión del archivo
                extension = Path(file_name).suffix  # incluye el punto, ej: ".pdf"

                # Si no tiene extensión, lo ignoramos (mismo comportamiento que tu script)
                if not extension:
                    continue

                # Normalizamos la extensión (sin el punto e en minúsculas)
                extension = extension[1:].lower()

                # Actualizamos contador
                extension_dirs[extension] += 1

                target_dir = base_path / extension
                if not target_dir.exists():
                    target_dir.mkdir(parents=True, exist_ok=True)

                source_file_path = base_path / file_name
                target_file_path = target_dir / file_name

                if target_file_path.exists():
                    # Mismo comportamiento: no sobrescribe, solo avisa
                    if verbose:
                        print(
                            f"[AVISO] El archivo '{file_name}' ya existe en '{target_dir}'. "
                            "No se moverá."
                        )
                    # Revertimos el conteo porque finalmente no movimos ese archivo
                    extension_dirs[extension] -= 1
                    if extension_dirs[extension] == 0:
                        del extension_dirs[extension]
                else:
                    shutil.move(str(source_file_path), str(target_file_path))
                    if verbose:
                        print(f"[OK] Movido: '{file_name}' -> '{target_dir}/'")

            except Exception as e:
                # Capturamos errores por archivo, así no se detiene todo el script
                print(f"[ERROR] Al organizar '{file_name}': {e}")

    return dict(extension_dirs)


def imprimir_resumen(extension_dirs: dict[str, int]) -> None:
    """Imprime el resumen de archivos organizados por extensión."""
    print("\nArchivos organizados con éxito.")
    print("Cantidad de archivos por extensión:")

    if not extension_dirs:
        print("No se movió ningún archivo.")
        return

    # Ordenamos por nombre de extensión para que sea más legible
    for ext in sorted(extension_dirs):
        count = extension_dirs[ext]
        print(f"  {ext}: {count} archivo(s)")


if __name__ == "__main__":
    # Puedes cambiar la ruta aquí o incluso leerla de una variable de entorno si quieres
    DIR_DESCARGAS = "."

    resumen = organizar_por_extension(DIR_DESCARGAS, verbose=True)
    imprimir_resumen(resumen)
