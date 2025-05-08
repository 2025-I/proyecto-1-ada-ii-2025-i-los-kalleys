[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kKWtV-CB)

# Proyecto 1 ADA II

## Integrantes

Juan Miguel Palacios | 2359321
Jhon Alexis Ruiz | 2266014
Nicolás Rodriguez | 2266071

## Descripción del Proyecto

Este proyecto resuelve dos problemas clásicos de programación mediante algoritmos eficientes aplicados a estructuras de texto y árboles.

### Problema 1: Subsecuencias más largas de un palíndromo

#### Descripción

Dada una cadena de caracteres de entrada, el objetivo es identificar y encontrar todas las subsecuencias que sean palíndromos y que tengan la mayor longitud posible.

Para la evaluación de las subsecuencias se deben ignorar:

- La diferencia entre caracteres en mayúsculas y minúsculas.
- Los caracteres que no sean alfanuméricos (como espacios, signos de puntuación, símbolos, etc.).

#### Formalización

Consideremos una cadena de entrada original S de longitud n.

Primero, se realiza un proceso de normalización sobre S para obtener una nueva cadena S'. Esta normalización implica:

1. Convertir todos los caracteres alfanuméricos a minúsculas.
2. Eliminar todos los caracteres que no sean alfanuméricos.

Por ejemplo, si S fuera "A man, a plan, a canal: Panama", la cadena normalizada S' sería "amanaplanacanalpanama".

Una subsecuencia P de S' se forma seleccionando cero o más caracteres de S' en su orden original, sin cambiar el orden relativo de los caracteres seleccionados.

Una subsecuencia P es palindrómica si se lee igual de izquierda a derecha que de derecha a izquierda.

El problema consiste en encontrar todas las subsecuencias P de S' que cumplen dos condiciones:

1. P es un palíndromo.
2. La longitud de P es la máxima posible entre todas las subsecuencias palindrómicas de S'.

Se deben reportar todas las subsecuencias que cumplan estas dos condiciones.

### Problema 2: Planeando una fiesta de la compañía

#### Descripción

Dada la estructura jerárquica de una empresa, que se puede visualizar como un árbol, el problema consiste en seleccionar a un grupo de empleados para invitarlos a una fiesta. El objetivo es que la suma total de las calificaciones de convivencia de los empleados invitados sea lo más alta posible. La restricción principal para seleccionar a los invitados es que no se puede invitar a un empleado si su supervisor directo también ha sido invitado.

#### Formalización

La estructura de la compañía se modela como un árbol enraizado.

- Los nodos del árbol representan a los empleados.
- Las conexiones (aristas) representan las relaciones de supervisión directa, apuntando del supervisor al empleado subordinado.
- Cada empleado (nodo) tiene una calificación de convivencia asociada, que es un número entero.

Se debe seleccionar un conjunto de empleados para invitar a la fiesta. Llamemos a este conjunto "Invitados".

La restricción es la siguiente: Si un empleado está en el conjunto "Invitados", ninguno de sus subordinados directos puede estar también en el conjunto "Invitados". Esta restricción se aplica únicamente a las relaciones de supervisión directa (padre-hijo en el árbol).

El objetivo es encontrar un conjunto "Invitados" que cumpla la restricción y cuya suma de las calificaciones de convivencia de todos los empleados en ese conjunto sea la máxima posible.

### Formato de entrada y salida

- Ambos problemas reciben su entrada desde un **archivo de texto** indicado por el usuario mediante un **selector de archivos (file chooser)**.
- La salida del programa se imprime por **salida estándar (stdout)** en minúsculas.

