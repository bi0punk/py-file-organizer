# Py File Organizer

Organizador de archivos que mueve archivos a subdirectorios según su extensión. Versiones CLI y GUI disponibles.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)

## Tabla de Contenidos

- [Características](#características)
- [Stack](#stack)
- [Estructura](#estructura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Configuración](#configuración)
- [CI](#ci)
- [Limitaciones / Roadmap](#limitaciones--roadmap)
- [Licencia](#licencia)

## Características

- **Versión CLI** (`console/main.py`): organiza archivos desde terminal
- **Versión GUI** (`gui/gui-version.py`): interfaz gráfica con Tkinter para seleccionar directorio
- Agrupa archivos en carpetas nombradas según su extensión (`.pdf` → `pdf/`, `.jpg` → `jpg/`)
- Manejo seguro de duplicados (no sobrescribe archivos existentes)
- Reporte detallado de archivos movidos por extensión
- Sin dependencias externas — solo standard library

## Stack

- **Python 3.11+** (standard library: `os`, `shutil`, `pathlib`, `tkinter`)
- GUI: Tkinter (incluido en Python)
- Linting: Ruff | Tests: pytest

## Estructura

```
py-file-organizer/
├── console/
│   └── main.py             # Versión CLI
├── gui/
│   └── gui-version.py      # Versión con interfaz gráfica
├── tests/
│   └── test_smoke.py       # Tests de humo
├── pyproject.toml           # Configuración del proyecto
├── requirements.txt         # Dependencias (vacío, sin externas)
├── .env.example             # Variables de entorno placeholder
├── .github/
│   └── workflows/
│       └── ci.yml           # CI: Ruff + pytest
├── LICENSE
└── README.md
```

## Requisitos

- Python >= 3.11
- Para la GUI: Tkinter (incluido en la mayoría de distribuciones; en Ubuntu/Debian: `sudo apt install python3-tk`)

## Instalación

```bash
git clone https://github.com/bi0punk/py-file-organizer.git
cd py-file-organizer
# Sin dependencias externas
```

## Uso

### CLI

Edita la variable `DIR_DESCARGAS` en `console/main.py` o pásala directamente:

```python
# console/main.py
DIR_DESCARGAS = "/ruta/al/directorio"  # <-- modifica aquí
```

```bash
python console/main.py
```

Ejemplo de ejecución:

```
[OK] Movido: 'documento.pdf' -> '/home/user/Descargas/pdf/'
[OK] Movido: 'foto.jpg' -> '/home/user/Descargas/jpg/'
[OK] Movido: 'script.py' -> '/home/user/Descargas/py/'

Archivos organizados con éxito.
Cantidad de archivos por extensión:
  jpg: 3 archivo(s)
  pdf: 1 archivo(s)
  py: 1 archivo(s)
```

### GUI

```bash
python gui/gui-version.py
```

Se abre una ventana. Haz clic en "Seleccionar Directorio", elige la carpeta y el programa organiza los archivos automáticamente.

## Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

## Configuración

No requiere variables de entorno. Modifica `DIR_DESCARGAS` en `console/main.py` para cambiar el directorio objetivo.

## CI

GitHub Actions ejecuta Ruff linting y pytest en cada push y pull request:

```yaml
- name: Ruff check
  run: uv run ruff check .
- name: Pytest
  run: uv run pytest -q
```

## Limitaciones / Roadmap

- No organiza archivos sin extensión
- CLI requiere editar el script para cambiar el directorio objetivo
- No soporta filtros por tipo de archivo ni expresiones regulares
- Futuro: argumento CLI `--path`, modo dry-run, deshacer operación, soporte para directorios anidados

## Licencia

MIT
