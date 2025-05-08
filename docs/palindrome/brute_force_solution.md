# Informe: `max_subsequence_palindrome`

## 📌 Descripción general

La función `max_subsequence_palindrome` encuentra la **subcadena palindrómica más larga** dentro de un texto dado. Utiliza un enfoque de fuerza bruta al generar todas las subcadenas posibles y verificar si son palíndromos mediante la función auxiliar `is_palindrome`.

---

## ⚙️ Funcionamiento paso a paso

1. **Inicialización**:
   - Se define `longest_palindrome` como una cadena vacía.
   - Se obtiene la longitud del texto con `text_length = len(text)`.

2. **Generación de subcadenas**:
   - Dos bucles anidados recorren todas las combinaciones posibles de índices `start` y `end`.
   - Cada subcadena se extrae con `text[start:end]`.

3. **Verificación de palíndromo**:
   - Se evalúa cada subcadena con `is_palindrome(substring)`.
   - Si la subcadena es un palíndromo y su longitud es mayor que la del actual `longest_palindrome`, se actualiza.

4. **Resultado**:
   - La función retorna `longest_palindrome`, el palíndromo más largo encontrado.

---

## ⏱️ Complejidad computacional

### Complejidad temporal

- Se generan `(n²)` subcadenas.
- Cada verificación de palíndromo toma hasta \( O(n) \) tiempo.
- Por lo tanto, la **complejidad temporal total** es:

`O(n³)`
