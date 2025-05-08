# Acción de GitHub: Configurar Python

Esta acción de GitHub configura Python 3.12 en el entorno del flujo de trabajo e instala las dependencias necesarias especificadas en un archivo `requirements.txt`, si existe.

## 📦 Workflow: Composite Action

**Archivo:** `.github/actions/setup-python/action.yml`

## Características

- Instala Python 3.12 utilizando la acción `actions/setup-python`.
- Actualiza `pip` a la última versión.
- Instala automáticamente las dependencias desde `requirements.txt` si el archivo está presente en el repositorio.

## Entradas

Esta acción no requiere entradas.

## Salidas

Esta acción no genera salidas.

## Uso

A continuación, se muestra el codigo YAML para utilizar la acción en los demas workflows:

```yaml
name: setup python
description: "Setup Python 3.12 and install dependencies"

runs:
  using: "composite"
  steps:
    - name: Set up Python 3.12
      uses: actions/setup-python@v3
      with:
        python-version: "3.12"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      shell: bash
```

## Pasos

1. **Configurar Python 3.12**  
   La acción utiliza `actions/setup-python@v3` para instalar Python 3.12 en el entorno del flujo de trabajo.

2. **Actualizar pip**  
   La acción actualiza `pip` a la última versión utilizando el comando:

   ```bash
   python -m pip install --upgrade pip
   ```

3. **Instalar dependencias**  
   Si existe un archivo `requirements.txt` en el repositorio, la acción instala las dependencias listadas en él utilizando:

   ```bash
   pip install -r requirements.txt
   ```

## Utilidad

Esta acción es útil para configurar rápidamente un entorno de Python en el flujo de trabajo de GitHub Actions, asegurando que todas las dependencias necesarias estén instaladas antes de ejecutar pruebas o implementaciones, evitando repetir la misma acción en diferentes puntos con una unica configuración.
