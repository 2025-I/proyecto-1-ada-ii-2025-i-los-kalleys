![Gráfico de tiempo de ejecución fuerza bruta - palíndromo](../imgs/solución%20fuerza%20bruta%20-%20palindromo.png)
## Solución fuerza bruta

Aunque el algoritmo de fuerza bruta implementado para detectar palíndromos tiene una complejidad teórica de **O(n³)**, el comportamiento observado en los experimentos muestra un crecimiento más cercano a una función **lineal**. Esta discrepancia se debe principalmente a que los tamaños de entrada utilizados (hasta `n = 1000`) no son lo suficientemente grandes como para que se manifieste plenamente el crecimiento cúbico predicho por la teoría.

Por tanto, se concluye que, aunque la complejidad del algoritmo sigue siendo O(n³), los resultados experimentales actuales no reflejan completamente este comportamiento.

---

![Gráfico de tiempo de ejecución dinamica - palíndromo](../imgs/solución%20dinámica%20-%20palindromo.png)

## Solución dinamica

El gráfico anterior muestra una comparación entre el tiempo **experimental** y el tiempo **teórico** esperado de la solución dinámica para detectar palíndromos.

#### Observaciones:
- Ambas líneas tienen un crecimiento cuadrático, lo que confirma que el algoritmo se comporta según lo esperado teóricamente.
- El tiempo experimental es **ligeramente superior** al teórico, probablemente debido a:
  - Costos adicionales de operaciones internas (acceso a memoria, condiciones, asignaciones).
  - Sobrecarga del entorno de ejecución (como el recolector de basura o el sistema operativo).

En conclusión La implementación dinámica del algoritmo de detección de palíndromos muestra un **buen ajuste con la complejidad teórica esperada**. Esto indica una solución eficiente y escalable para tamaños de entrada grandes, a diferencia de la solución fuerza bruta que presentaba un crecimiento cúbico mucho más costoso.

---

![Gráfico de tiempo de ejecución voraz - palíndromo](../imgs/solución%20voraz%20-%20palindromo.png)

## Solución voraz

El gráfico compara el tiempo **experimental** y el tiempo **teórico** esperado para la solución voraz en la detección del palíndromo más largo en una cadena.

#### Observaciones:
- Se observa que el **comportamiento experimental es notablemente mejor** que lo que sugiere la curva teórica, incluso para entradas grandes.

#### Razones del buen rendimiento:
- El algoritmo **no almacena subproblemas**, ni utiliza estructuras de datos pesadas.
- La función `expand_center` **se ejecuta menos veces de lo esperado** en la mayoría de los casos prácticos, especialmente cuando no hay muchos caracteres repetidos alrededor del centro.
- El uso de variables locales y estructuras simples hace que la implementación sea **altamente optimizada a nivel de ejecución**.
- La condición `text[i] == text[i + 1]` permite **saltarse iteraciones innecesarias**, lo que reduce el número total de comparaciones.

#### Conclusión:
Aunque teóricamente este algoritmo tiene una complejidad cuadrática, **en la práctica se comporta casi linealmente para muchas entradas**, lo que lo convierte en una solución altamente eficiente y útil.
