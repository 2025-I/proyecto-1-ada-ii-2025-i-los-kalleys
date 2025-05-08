from typing import List

def greedy_party(adj_matrix: List[List[int]], conv_list: List[int]) -> str:
    number_employees: int = len(adj_matrix)

    invited: list = [0] * number_employees
    blocked: list = [False] * number_employees

    supervisors: List[List[int]] = {i: [] for i in range(number_employees)}
    subordinates: List[List[int]] = {i: [] for i in range(number_employees)}

    for i in range(number_employees):
        for j in range(number_employees):
            if adj_matrix[i][j] == 1:
                subordinates[i].append(j)
                supervisors[j].append(i)

    order: list = sorted(range(number_employees), key=lambda i: conv_list[i], reverse=True)

    for i in order:
        if not blocked[i] and all(invited[sup] == 0 for sup in supervisors[i]) and all(invited[sub] == 0 for sub in subordinates[i]):
            invited[i] = 1
            blocked[i] = True
            for n in supervisors[i] + subordinates[i]:
                blocked[n] = True

    conv_total: int = sum(conv_list[i] for i in range(number_employees) if invited[i] == 1)
    invited[:-1].append(conv_total)
    return invited + [conv_total]

# Ejemplos de uso
matriz1 = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
conv1 = [10, 30, 15, 5, 8]

matriz2 = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
conv2 = [12, 18, 5, 10, 8, 7]

matriz3 = [
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
]

conv3 = [12, 2, 5, 11, 11, 0]

# print(greedy_party(matriz1, conv1))
# print(greedy_party(matriz2, conv2))
# print(greedy_party(matriz3, conv3))

adj_matrix: list[list[int]] = [
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

weights: list[int] =  [2, 7, 9, 7, 5, 3, 6, 8, 9, 2]
