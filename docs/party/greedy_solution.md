# Informe de la Función `greedy_party`

## Objetivo General

La función `greedy_party` implementa una estrategia **voraz (greedy)** para seleccionar un subconjunto de empleados que maximice la convivencia total en una fiesta, bajo la restricción de que **no pueden asistir empleados que tengan una relación directa de supervisión o subordinación** entre sí.

Esta función es útil en escenarios donde se quiere una solución rápida y razonablemente buena (aunque no necesariamente óptima) a un problema de selección con restricciones jerárquicas.

Se decide invitar por el mayor valor de convivencia confiando en que hará parte de la solución global que busca maximizar dichos valores de convivencia, la cuestión es que esta premisa en este problema no se cumple necesariamente, asi que la solución voraz no nos garantiza la solución optima
---

## Funcionalidad de la Función

### Inicialización

- Se crean listas auxiliares:
  - `invited`: lista binaria (`0` o `1`) que indica si cada empleado ha sido invitado.
  - `blocked`: lista booleana que marca a los empleados que no pueden ser invitados por conflictos jerárquicos o ya invitados

- Se construyen dos diccionarios:
  - `supervi`: para cada empleado, guarda la lista de sus supervisores.
  - `subordin`: para cada empleado, guarda la lista de sus subordinados.

Esto se basa en una **matriz de adyacencia** `adj_matrix`, donde `adj_matrix[i][j] == 1` indica que el empleado `i` supervisa al empleado `j`.

### Ordenamiento por convivencia

Los empleados se ordenan de mayor a menor según su puntuación de convivencia (`conv_list`). Este orden define la prioridad en la selección voraz.

### Selección Voraz

Se recorre a los empleados en orden descendente de convivencia. Un empleado `i` será invitado si:

1. No está bloqueado (`blocked[i] == False`).
2. Ninguno de sus supervisores ni subordinados ha sido invitado (`invited[sup] == 0` y `invited[sub] == 0`).

Si se invita al empleado:
- Se lo marca como invitado.
- Se bloquea a él y a todos sus supervisores y subordinados para evitar conflictos jerárquicos.

## Complejidad

1. **Construcción de diccionarios de supervisores y subordinados**  
   Se recorren todos los pares `(i, j)` en la matriz `adj_matrix`, lo que toma:  
   **O(n²)**

2. **Ordenamiento por convivencia**  
   Se ordena la lista de empleados en función de su valor de convivencia:  
   **O(n log n)**

3. **Selección voraz de invitados**  
   En el peor caso, para cada empleado se verifica su estado y el de sus subordinados/supervisores (hasta `n` en total), lo que resulta en:  
   **O(n²)**

4. **Cálculo de la convivencia total**  
   Se recorre una vez la lista de empleados:  
   **O(n)**

**Complejidad total:**  
**O(n²)**





