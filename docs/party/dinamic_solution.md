# 📊 Informe: Análisis de la función `max_dinamic_invite_values`

## 📌 Objetivo

La función `max_dinamic_invite_values` tiene como propósito resolver el problema de **seleccionar un subconjunto óptimo de empleados** a invitar a un evento, basado en una relación jerárquica representada como un árbol y una lista de valores asignados a cada empleado. No se puede invitar a un subordinado si su jefe ya fue invitado.

---

## ⚙️ Funcionamiento

El algoritmo consta de varias etapas claramente diferenciadas, cada una delegada en una función:

### 1. `build_dependency_graph(matrix)`
- Construye un grafo dirigido (`dependency_graph`) donde cada nodo representa un empleado, y hay una arista `i → j` si `i` es jefe de `j`.
- También calcula el número de dependencias (`dependency_count`) de cada nodo.

### 2. `topological_sort(...)`
- Realiza un **ordenamiento topológico** del grafo utilizando una cola para procesar nodos sin dependencias primero.
- Esto asegura que los subordinados siempre se procesen después que sus jefes.

### 3. `calculate_optimal_values(...)`
- Recorre el grafo en orden inverso al topológico (de hojas a raíz).
- Para cada empleado:
  - Calcula el valor si **no es invitado** (`skip_current`).
  - Calcula el valor si **es invitado** (`invite_current`), evitando invitar a subordinados.
- Guarda para cada empleado una tupla `(mejor_sin_invitar, mejor_con_invitar)`.

### 4. `reconstruct_solution(...)`
- Usando DFS y las decisiones anteriores, reconstruye el conjunto óptimo de empleados a invitar.
- Se asegura de que si un jefe es invitado, sus subordinados no lo sean.

### 5. Resultado final
- Devuelve una lista binaria con `1` si el empleado fue invitado y `0` si no, más un elemento extra al final con la **suma total de valores** de los empleados invitados.

---

## ⏱️ Complejidad Temporal

| Función | Complejidad | Justificación |
|--------|-------------|---------------|
| `build_dependency_graph` | O(n²) | Recorre toda la matriz `n x n` |
| `topological_sort` | O(n) | recorre todos los nodos |
| `calculate_optimal_values` | O(n) | Cada nodo y sus hijos se visitan una vez |
| `reconstruct_solution` | O(n) | DFS en árbol |
| `max_dinamic_invite_values` (total) | **O(n²)** | Dominado por construcción del grafo |

Donde `n` es el número de empleados

`Para una complejidad temporal de O(n²)`