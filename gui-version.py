import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def organize_files(directory):
    try:
        extension_dirs = {}
        for file_name in os.listdir(directory):
            try:
                extension = os.path.splitext(file_name)[1]
                if extension:
                    extension = extension[1:]  # Eliminar el punto inicial de la extensión
                    if extension in extension_dirs:
                        extension_dirs[extension] += 1
                    else:
                        extension_dirs[extension] = 1
                    target_dir = os.path.join(directory, extension)
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    source_file_path = os.path.join(directory, file_name)
                    target_file_path = os.path.join(target_dir, file_name)
                    if os.path.exists(target_file_path):
                        print(f"El archivo '{file_name}' ya existe en el directorio de destino.")
                    else:
                        # Mover el archivo al directorio correspondiente
                        shutil.move(source_file_path, target_file_path)
            except Exception as e:
                print(f"Error al organizar el archivo '{file_name}': {str(e)}")
        result = "Archivos organizados con éxito.\n\nCantidad de archivos por extensión:\n"
        for ext, count in extension_dirs.items():
            result += f"{ext}: {count} archivo(s)\n"
        messagebox.showinfo("Resultado", result)
    except Exception as e:
        messagebox.showerror("Error", f"Error al organizar los archivos: {str(e)}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

def create_gui():
    root = tk.Tk()
    root.title("Organizador de Archivos")
    root.geometry("400x200")
    
    label = tk.Label(root, text="Seleccione el directorio a organizar:")
    label.pack(pady=20)
    
    select_button = tk.Button(root, text="Seleccionar Directorio", command=select_directory)
    select_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
