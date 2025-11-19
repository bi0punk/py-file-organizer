import os
import shutil
from pathlib import Path
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def organize_files(directory: str) -> str:
    """
    Organiza los archivos de `directory` en subcarpetas según su extensión.

    - Crea una carpeta por cada extensión (sin punto, en minúsculas).
    - Mueve los archivos a la carpeta correspondiente.
    - No sobrescribe archivos ya existentes.
    - Devuelve un resumen en texto.
    """
    base_path = Path(directory).expanduser().resolve()

    if not base_path.exists():
        raise FileNotFoundError(f"El directorio '{base_path}' no existe.")

    if not base_path.is_dir():
        raise NotADirectoryError(f"'{base_path}' no es un directorio válido.")

    extension_dirs: dict[str, int] = defaultdict(int)
    duplicated_files = 0
    files_without_extension = 0
    errors: list[str] = []

    # Usamos scandir para mejor rendimiento
    with os.scandir(base_path) as entries:
        for entry in entries:
            # Sólo trabajamos con archivos regulares (no directorios, no enlaces)
            if not entry.is_file():
                continue

            file_name = entry.name
            try:
                extension = Path(file_name).suffix  # incluye el punto, ej: ".pdf"
                if not extension:
                    files_without_extension += 1
                    continue

                # Normalizamos extensión (sin punto, en minúsculas)
                extension = extension[1:].lower()

                # Actualizamos conteo
                extension_dirs[extension] += 1

                target_dir = base_path / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                source_file_path = base_path / file_name
                target_file_path = target_dir / file_name

                if target_file_path.exists():
                    # No sobrescribimos: lo contamos como duplicado y restamos del conteo
                    duplicated_files += 1
                    extension_dirs[extension] -= 1
                    if extension_dirs[extension] == 0:
                        del extension_dirs[extension]
                    continue

                shutil.move(str(source_file_path), str(target_file_path))

            except Exception as e:
                errors.append(f"- {file_name}: {e!s}")

    # Construimos el resumen
    lines = []
    lines.append("Archivos organizados con éxito.\n")
    lines.append("Cantidad de archivos por extensión:\n")

    if extension_dirs:
        for ext in sorted(extension_dirs):
            count = extension_dirs[ext]
            lines.append(f"  {ext}: {count} archivo(s)")
    else:
        lines.append("  No se movió ningún archivo con extensión válida.")

    lines.append("\nDetalles adicionales:")
    lines.append(f"  Archivos sin extensión: {files_without_extension}")
    lines.append(f"  Archivos duplicados no movidos: {duplicated_files}")

    if errors:
        lines.append("\nSe encontraron errores al procesar algunos archivos:")
        lines.extend(errors)

    return "\n".join(lines)


def select_directory(root: tk.Tk, status_var: tk.StringVar):
    directory = filedialog.askdirectory(title="Seleccionar directorio a organizar")
    if not directory:
        return  # Usuario canceló

    try:
        status_var.set("Organizando archivos, por favor espere...")
        root.update_idletasks()

        result_text = organize_files(directory)

        messagebox.showinfo("Resultado", result_text)
        status_var.set("Organización completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al organizar los archivos:\n{e!s}")
        status_var.set("Ocurrió un error.")


def create_gui():
    root = tk.Tk()
    root.title("Organizador de Archivos")
    root.geometry("420x200")
    root.resizable(False, False)

    # Centrar ventana en pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Estilo básico con ttk
    try:
        ttk.Style().theme_use("clam")
    except Exception:
        pass

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill="both")

    label = ttk.Label(frame, text="Seleccione el directorio que desea organizar por extensión:")
    label.pack(pady=(0, 15))

    status_var = tk.StringVar(value="Listo.")

    select_button = ttk.Button(
        frame,
        text="Seleccionar Directorio",
        command=lambda: select_directory(root, status_var)
    )
    select_button.pack(pady=10)

    status_label = ttk.Label(frame, textvariable=status_var, foreground="gray")
    status_label.pack(pady=(10, 0))

    root.mainloop()


if __name__ == "__main__":
    create_gui()
