# 🐍 Proyecto Python – Integración Continua

Este repositorio contiene un proyecto en Python que utiliza **GitHub Actions** para automatizar procesos de verificación de código y ejecución. A través de un archivo `build.yml`, se define un flujo de trabajo que se activa en cambios a la rama principal.

---

## 📦 Workflow: Build Project

**Archivo:** `.github/workflows/build.yml`

Este flujo de trabajo realiza las siguientes tareas:

- Se activa en `push` y `pull request` hacia la rama `main`.
- Verifica el estilo del código fuente con `flake8`.
- Ejecuta el archivo principal del proyecto (`src/main.py`).
- Usa una acción compuesta para configurar Python y sus dependencias.

---

## 🧪 Disparadores

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

Este bloque indica que el flujo de trabajo se ejecutará automáticamente cuando:

- Se haga un push a la rama main.
- Se cree o actualice una pull request hacia main.

## 🔄 Pasos del workflow

1. Checkout del código fuente

```yml
- name: Checkout code
  uses: actions/checkout@v4
```

Descarga el código del repositorio en el entorno del runner.

## 2. Configurar Python (acción compuesta personalizada)

```yml
- name: Setup python
  uses: ./.github/actions/setup-python
```

## 3. Analizar estilo de código con Flake8

```yml
- name: Lint with flake8
  run: flake8 . --count --statistics --max-line-length=127 --max-complexity=10 --ignore=E203,W503
```

Ejecuta flake8 con parámetros que:

- Ignoran advertencias comunes en proyectos con PEP8 flexible (E203, W503).
- Permiten líneas más largas (hasta 127 caracteres).
- Limitan la complejidad ciclomática de funciones a 10.

## 4. Ejecutar el programa principal

```yml
- name: Run project
  run: python src/main.py
```

Lanza el archivo src/main.py, que debe ser el punto de entrada de tu aplicación.

## ✅ Resultados esperados

Al ejecutar este flujo:

- Se valida automáticamente el estilo del código.
- Se asegura que el programa principal corre sin errores.
- Se integran buenas prácticas de CI/CD desde el inicio del proyecto.
