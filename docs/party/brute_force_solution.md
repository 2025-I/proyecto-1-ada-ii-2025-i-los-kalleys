## Informe: Análisis de la función `brute_force_party`

### Descripción general

La función `brute_force_party` busca formar el grupo de empleados más compatible para una fiesta, basándose en una matriz que representa relaciones jerárquicas (supervisor-subordinado) y una lista de valores de compatibilidad individuales. El objetivo es **maximizar la suma de compatibilidades** sin incluir a dos personas donde una supervise a la otra.

---

### Estructura del algoritmo

El proceso se puede dividir en los siguientes pasos principales:

1. **Construcción del grafo** (`build_graph`):  
   Se genera un conjunto de pares inválidos (`invalid_pairs`) que representan relaciones prohibidas entre empleados, derivados de la matriz de supervisión.

2. **Generación de subconjuntos**:  
   Se generan todos los subconjuntos posibles de empleados (excepto el conjunto vacío) mediante combinaciones (`itertools.combinations`).

3. **Validación de grupos** (`is_valid_group`):  
   Se verifica que ningún grupo seleccionado contenga una relación supervisor-subordinado.

4. **Cálculo de compatibilidad total** (`compute_total_compatibility`):  
   Si el grupo es válido, se calcula la suma de compatibilidades.

5. **Selección del mejor grupo**:  
   Se actualiza el grupo óptimo si la compatibilidad total supera al máximo registrado.

6. **Resultado final**:  
   Se devuelve un vector binario indicando los empleados seleccionados, seguido por el valor de compatibilidad total como último elemento de la lista.

---

### Complejidad computacional

La complejidad de la solución es **exponencial**, más precisamente:

- Se generan todos los subconjuntos de los `n` empleados, lo que implica `2^n - 1` combinaciones.
- Para cada subconjunto:
  - Validar si es válido requiere revisar como máximo `O(m)` pares, donde `m` representa todas las parejas padre-hijo conectadas en el arbol (en el peor caso).
  - Calcular la compatibilidad toma `O(n)` en el peor caso.

**Complejidad total:** O(2^n · n)


---

### Conclusión

Esta implementación representa una **solución por fuerza bruta** al problema de maximización de compatibilidad con restricciones jerárquicas. Aunque garantiza encontrar la solución óptima, **no es eficiente para entradas grandes** debido a su **complejidad exponencial**. Sin embargo, puede ser útil como solución de referencia o en casos con pocos empleados (n pequeño).