# Documentación del Action: Codacy Security Scan

Este archivo de workflow de GitHub Actions está diseñado para ejecutar un análisis de seguridad utilizando **Codacy Analysis CLI** y subir los resultados en formato SARIF para integrarse con el escaneo de código de GitHub.

## 📦 Workflow: Codacy Scan

#### **Archivo:** `.github/workflows/codacy.yml`

### Nombre del Workflow

```yaml
name: Codacy Security Scan
```

El nombre del workflow es `Codacy Security Scan`.

---

### Eventos que Disparan el Workflow

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

El workflow se ejecuta en los siguientes casos:

- Cuando se realiza un `push` a la rama `main`.
- Cuando se abre o actualiza un `pull_request` hacia la rama `main`.

---

### Permisos

```yaml
permissions:
  contents: read
```

El workflow requiere permisos de solo lectura para los contenidos del repositorio.

---

### Jobs

El workflow define un único job llamado `codacy-security-scan`.

#### Configuración del Job

```yaml
jobs:
  codacy-security-scan:
    permissions:
      contents: read
      security-events: write
      actions: read
    name: Codacy Security Scan
    runs-on: ubuntu-latest
```

- **Permisos del Job**:
  - `contents: read`: Permite leer los contenidos del repositorio.
  - `security-events: write`: Permite escribir eventos de seguridad, necesarios para subir los resultados SARIF.
  - `actions: read`: Permite leer las acciones utilizadas en el workflow.
- **Ejecución**: El job se ejecuta en un runner de GitHub con el sistema operativo `ubuntu-latest`.

---

### Pasos del Job

El job consta de tres pasos principales:

1. **Checkout del Código**

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v4
   ```

   Este paso utiliza la acción oficial `actions/checkout` para clonar el repositorio en el runner.

2. **Ejecutar Codacy Analysis CLI**

   ```yaml
   - name: Run Codacy Analysis CLI
     uses: codacy/codacy-analysis-cli-action@v4
     with:
       project-token: ${{ secrets.CODACY_PROJECT_TOKEN }}
       verbose: true
       output: results.sarif
       format: sarif
       gh-code-scanning-compat: true
       max-allowed-issues: 2147483647
   ```

   Este paso ejecuta el análisis de seguridad utilizando la acción `codacy/codacy-analysis-cli-action`. Los parámetros configurados son:

   - `project-token`: Token del proyecto almacenado en los secretos del repositorio (`CODACY_PROJECT_TOKEN`).
   - `verbose`: Habilita la salida detallada del análisis.
   - `output`: Especifica el archivo de salida (`results.sarif`).
   - `format`: Define el formato de salida como `sarif`.
   - `gh-code-scanning-compat`: Habilita la compatibilidad con el escaneo de código de GitHub.
   - `max-allowed-issues`: Establece el número máximo de problemas permitidos (valor máximo: `2147483647`).

3. **Subir Resultados SARIF**

   ```yaml
   - name: Upload SARIF results file
     uses: github/codeql-action/upload-sarif@v3
     with:
       sarif_file: results.sarif
   ```

   Este paso utiliza la acción `github/codeql-action/upload-sarif` para subir el archivo SARIF generado (`results.sarif`) al escaneo de código de GitHub.

---

## Resumen

Este workflow automatiza el análisis de seguridad del código fuente utilizando Codacy y sube los resultados en formato SARIF para integrarse con las herramientas de escaneo de código de GitHub. Es ideal para garantizar la seguridad del código en cada cambio realizado en la rama principal (`main`).
