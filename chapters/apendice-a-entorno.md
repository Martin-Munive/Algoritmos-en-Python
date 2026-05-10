# Apendice A. Entorno de trabajo

Este libro usa Python como lenguaje principal.

La edicion web esta construida con Jupyter Book y publicada como sitio estatico en GitHub Pages.

## Requisitos locales

Para construir el libro:

```bash
pip install -r requirements.txt
jupyter-book build .
```

La salida HTML se genera en:

```text
_build/html
```

## Nota

No todos los capitulos necesitan ser notebooks. La regla editorial es usar notebooks cuando ejecutar codigo sea parte esencial del aprendizaje, y Markdown cuando el objetivo sea explicar, ordenar o argumentar.
