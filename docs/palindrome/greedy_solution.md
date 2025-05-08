# Informe: Análisis de la función `greedy_palindromic_substring`

## 📌 Objetivo

La función `greedy_palindromic_substring(text: str) -> str` tiene como propósito encontrar de forma eficiente un **subpalíndromo más largo** dentro de una cadena, utilizando un enfoque **voraz (greedy)** y expansión desde el centro.
Por lo cual como estrategia voraz, se empezó a ver desde cada caracter como si fuera el centro del palindromo, asi expandiendo desde su centro todos tendrían que dar iguales hasta que finalice el palindromo. También se analizó con una mejora basada en la detección de caracteres repetidos consecutivos, eso haria que fuera palindrome hasta sus extremos y poder expandir desde ahí.

Nota: debido a que el problema no cumple con los requerimientos para poder implementar una estrategia voraz efectiva se implementó la estrategia voraz en el sentido local de cada caracter, aunque para dar una solucion completa decidimos conservar esos resultados y al final retornar la mejor. De manera que pese a que el algoritmo no es completamente voraz, ya que evalúa múltiples opciones (todos los centros posibles), pero toma decisiones locales (expandir alrededor de un centro) sin retroceder. Con esa idea nos permitimos establecer este algoritmo que nos entrega la solución global del problema.

---

## ⚙️ Funcionamiento

La estrategia se basa en detectar centros de posibles palíndromos y expandirse hacia los extremos mientras los caracteres coincidan.

### 1. Variables principales
- `best`: guarda el palíndromo más largo encontrado.
- `equal_count`: cuenta cuántos caracteres consecutivos son iguales.

### 2. Función `expand_center(current_i)`
- Calcula los índices `left` y `right` desde donde expandir.
- Mientras `text[left] == text[right]`, se sigue expandiendo.
- Devuelve el subpalíndromo encontrado en esa expansión.

### 3. Recorriendo la cadena
- Se recorre cada índice `i` de la cadena.
- Si el carácter actual es igual al siguiente, se incrementa `equal_count` (para manejar casos como `"aa"`).
- Si no, se expande desde `i`, se reinicia `equal_count` y se actualiza el mejor palíndromo si el nuevo es más largo.

---

## ⏱️ Complejidad Temporal

| Sección | Complejidad |
|--------|-------------|
| Recorrido principal (`for i in range(len(text))`) | O(n) |
| Cada llamada a `expand_center` | En el peor caso O(n) |
| Comparación de strings con `max(..., key=len)` | O(n) en el peor caso |

### ✅ Complejidad total:
En total para el peor caso cada carácter es comparado al menos una vez por cada expansión, lo que da: O(n²) en el peor caso