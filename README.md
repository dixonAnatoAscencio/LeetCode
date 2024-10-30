# LeetCode

# Big (O) - Time and Space Complexity 

Time complexity: describes the amount of time necessary to execute an algorithm 

Space Complexity: describes amount of memory or space utilized by an algorithm/program

Both - asymptotically
In computer science, big O notations is used to describe algorithms according to how fast they run (time complexity) or how much space they take (space complexity) as the input size grows.

Technical Definition: Big O is a mathematical notation that describes the limiting behaviour of a function when the argument tends towards a paticular value of infinity

Why do we need Big O? - Big O notation helps us understand how the performance of an algorithm changes as the size of the input grows, providing a simple way to compare and analyse different algorithms' efficiency


# Big O Summary

 # O(1) - Complejidad Constante
Descripción: La complejidad constante significa que el tiempo de ejecución de la operación no depende del tamaño de la entrada. No importa si la entrada es de tamaño 10 o 10,000; el tiempo de ejecución es el mismo.
Ejemplo: Acceder a un elemento en un array por su índice, como array[5], siempre toma el mismo tiempo sin importar el tamaño del array.

```python
def get_first_element(arr):
    return arr[0]  # O(1)
```

# O(log N) - Complejidad Logarítmica
Descripción: La complejidad logarítmica se reduce con el tamaño de la entrada a medida que crece. Cada operación reduce significativamente el tamaño del problema, como en una búsqueda binaria, dividiendo la entrada en dos partes en cada paso.
Ejemplo: Búsqueda binaria en un array ordenado. Si se tiene un array de 16 elementos, se necesitarán como máximo 4 pasos para encontrar el elemento buscado.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # O(log N)


# O(N) - Complejidad Lineal
Descripción: En complejidad lineal, el tiempo de ejecución crece proporcionalmente al tamaño de la entrada. Si la entrada se duplica, el tiempo de ejecución también se duplica.
Ejemplo: Recorrer un array y sumar todos sus elementos

def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total  # O(N)



# O(N log N) - Complejidad Linearítmica
Descripción: La complejidad linearítmica es típica de algoritmos de ordenamiento eficientes, como Merge Sort y Quick Sort. El tiempo de ejecución es mayor que el lineal, pero menor que el cuadrático.
Ejemplo: Algoritmo Merge Sort para ordenar una lista.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)  # O(N log N)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left or right)
    return sorted_arr


# O(N²) - Complejidad Cuadrática
Descripción: La complejidad cuadrática aparece en algoritmos donde cada elemento de la entrada se compara con cada otro elemento. Si el tamaño de la entrada aumenta, el tiempo de ejecución aumenta cuadráticamente.
Ejemplo: Algoritmo Bubble Sort para ordenar una lista.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # O(N^2)
    return arr


# O(2^N) - Complejidad Exponencial
Descripción: En complejidad exponencial, el tiempo de ejecución se duplica con cada incremento en el tamaño de entrada. Esta complejidad es ineficiente para entradas grandes y es común en problemas de combinatoria.
Ejemplo: Resolver el problema de la subsecuencia (subconjunto) en un conjunto de números.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # O(2^N)


# O(N!) - Complejidad Factorial
Descripción: La complejidad factorial es extremadamente alta. Suele aparecer en algoritmos que generan todas las permutaciones posibles de una lista.
Ejemplo: Resolver el problema del "viajante de comercio" generando todas las rutas posibles para minimizar la distancia total.

import itertools

def traveling_salesman(points):
    shortest_route = float("inf")
    for route in itertools.permutations(points):
        distance = calculate_distance(route)
        shortest_route = min(shortest_route, distance)
    return shortest_route  # O(N!)

def calculate_distance(route):
    # Calcula la distancia total de una ruta
    return sum(
        ((route[i][0] - route[i+1][0]) ** 2 + (route[i][1] - route[i+1][1]) ** 2) ** 0.5
        for i in range(len(route) - 1)
    )








