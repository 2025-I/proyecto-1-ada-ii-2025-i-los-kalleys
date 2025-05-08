# Informe: Análisis de la función `max_dynamic_palindrome`

## 📌 Objetivo

La función `max_dynamic_palindrome(phrase: str) -> str` tiene como propósito encontrar el **subpalíndromo más largo** dentro de una cadena de texto utilizando **programación dinámica**.

---

## ⚙️ Funcionamiento

La lógica principal se basa en construir una **matriz booleana** `matrix[i][j]` que indica si la subcadena `phrase[i:j+1]` es un palíndromo.

### 1. Inicialización
- Se define la longitud de la frase (`phrase_len`).
- Si la longitud es 1 o menor, se retorna directamente.
- Se crea una matriz `matrix` de tamaño `n × n` inicializada en `False`.

### 2. Casos base
- Toda subcadena de longitud 1 es un palíndromo, por lo que se marca `matrix[i][i] = True`.

### 3. Llenado de la matriz
- Se recorren todas las posibles longitudes de subcadenas desde 2 hasta `n`.
- Para cada subcadena de longitud `substr_len`, se evalúa si es un palíndromo:
  - Si `phrase[i] == phrase[j]` y `matrix[i+1][j-1]` es verdadero, entonces `matrix[i][j] = True`.

### 4. Seguimiento del resultado
- Durante el recorrido, si se detecta un nuevo palíndromo más largo, se actualizan los valores de `start` y `max_length`.

### 5. Retorno
- Finalmente, se devuelve la subcadena comprendida entre `start` y `start + max_length`.

---

## ⏱️ Complejidad Temporal

### Análisis de cada sección:

| Sección | Complejidad |
|--------|-------------|
| Creación de la matriz `n x n` | O(n²) |
| Llenado de diagonal `matrix[i][i]` | O(n) |
| Doble bucle para subcadenas | O(n²) |
| Comparaciones y asignaciones dentro del bucle | O(1) por iteración |

### ✅ Complejidad total:

**O(n²)**