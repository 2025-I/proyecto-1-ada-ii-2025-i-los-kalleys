# Informe General de los Tests


El sistema permite probar la funcionalidad y el rendimiento de nuestros algoritmos sobre los distintos problemas (palíndromos y party), manteniendo separación entre generación de entrada, validación y medición de rendimiento.

Manejamos un sistema de pruebas para evaluar y comparar las soluciones mediante pruebas unitarias que repetimos Utilizando una clase base `TestRepetition` que permite:

- Ejecutar pruebas múltiples veces para obtener tiempos de ejecución promedio.
- Validar los resultados usando funciones inyectadas.
- Medir rendimiento con diferentes tamaños de entrada.

### Clase Base: `TestRepetition`

Esta clase hereda de `unittest.TestCase` nos permite probar algoritmos repetidamente. Sus principales métodos son:

- `setAlgorithm(algorithm, generate_test, validate)`: Define el algoritmo, el generador de casos y la función de validación.
- `run_n_repetitions(num_tests, repetitions=5)`: Ejecuta `repetitions` veces, una prueba con `num_tests` elementos y mide el tiempo promedio.
- `run_all_tests(sizes)`: Ejecuta `run_n_repetitions` con diferentes tamaños.

Las clases de test heredan de `TestRepetition` y sobreescriben:

- `setUp()`: Para establecer el algoritmo, generador de entrada y validador.
- `validate()`: Devuelve una función que realiza la validación de resultados.
- Métodos `test_*()`: Para pruebas específicas como tests pequeños (`toy`) que se pide o pruebas de rendimiento.
---

### consideraciones

validate en tests grandes de party: Cuando expected es None, hace que la validación se enfoque en la estructura del resultado debido a que se generan los casos y estos pueden tener multiples soluciones validas 

Soluciones no óptimas: Como la solución voraz de party no garantiza el óptimo, para la prueba voraz toy de party se usa una entrada estática (adj_matrix_greedy_solution) en test_toy, pues tenemos la limitación de que no obtenemos la solucion global asegurada.

Pruebas de rendimiento: Se imprimen tiempos promedio de ejecución para evaluar la eficiencia solo de tamaño 100 en adelante, hasta donde los algoritmos lo permiten. El de fuerza bruta party debido a su complejidad solo ejecutamos la prueba toy.

