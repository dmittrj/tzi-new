import numpy as np
import itertools

# Ваша матрица смежности
# Значение -1 означает, что между вершинами нет ребра
adj_matrix = np.array([
    [-1, -1, 0.2, 0.6], # Вершина 1
    [-1, -1, -1, -1],   # Вершина 2
    [-1, 0.8, -1, -1],  # Вершина 3
    [-1, 0.8, -1, -1]   # Вершина 4
])

for sublist in adj_matrix:
    for i in range(len(sublist)):
        if sublist[i] == -1:
            sublist[i] = float('inf')

start = int(input("Введите номер начальной вершины: ")) - 1
end = int(input("Введите номер конечной вершины: ")) - 1

paths = list()
for i in range(len(adj_matrix)):
    paths.extend(list(itertools.permutations(range(len(adj_matrix)), i + 1)))

paths = [path for path in paths if path[0] == start and path[-1] == end]

def path_product(path, matrix):
    product = 1
    for i in range(len(path) - 1):
        if matrix[path[i]][path[i+1]] == 0:
            return float('inf')
        product *= matrix[path[i]][path[i+1]]
    return product

min_product = float('inf')
min_path = None
for path in paths:
    product = path_product(path, adj_matrix)
    if product < min_product:
        min_product = product
        min_path = path

if min_path is not None:
    print("Минимальный путь: ", [vertex+1 for vertex in min_path])
    print("Произведение весов на этом пути: ", min_product)
else:
    print("Путь не найден")
