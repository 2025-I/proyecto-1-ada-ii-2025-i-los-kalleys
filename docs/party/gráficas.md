## Análisis del comportamiento experimental vs teórico  
**Solución Dinámica – Problema del Party**  
![Gráfico de tiempo de ejecución - Solución Dinámica Party](../imgs/solución%20dinamica%20-%20party.png)

Este gráfico compara el tiempo **experimental** y el tiempo **teórico** de ejecución para la función `max_dynamic_invite_values`, una implementación basada en programación dinámica aplicada al problema del "Party".

#### Observaciones:
- Ambas líneas presentan una **trayectoria creciente muy similar**, lo cual confirma que el comportamiento práctico **se alinea estrechamente con la predicción teórica**.


En conclusion el análisis muestra que la solución dinámica tiene un **comportamiento experimental que respalda su complejidad teórica O(n²)**.



![Gráfico de tiempo de ejecución voraz - palíndromo](../imgs/solución%20voraz%20-%20party.png)
## Solución voraz

El gráfico compara el tiempo **experimental** y el tiempo **teórico** esperado para la solución voraz en la busqueda de maximizar los valores de convivencia en un problema con restricciones especificas.

#### Observaciones:
- Se observa que el **comportamiento experimental es acorde al teorico esperado**
- Ambas líneas tienen un crecimiento cuadrático, lo que confirma que el algoritmo se comporta según lo esperado teóricamente.
- El algoritmo no utiliza programación dinámica ni recursión, lo que le permite tener un recorrido simple y directo.
- La construcción de las listas supervi y subordin permite un acceso rápido a relaciones jerárquicas, lo que reduce la necesidad de búsquedas repetidas en la matriz de adyacencia.
- El uso de blocked[i] permite evitar evaluaciones innecesarias al marcar empleados ya afectados por decisiones anteriores

**Conclusión**
Aunque este algoritmo no garantiza una solución óptima, su enfoque directo y sin estructuras complejas lo hace rápido y práctico para entradas grandes, especialmente cuando se requiere una decisión aproximada con bajo costo computacional. Es una solución útil en escenarios donde la eficiencia es más importante que la precisión absoluta.