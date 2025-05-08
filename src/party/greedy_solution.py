from typing import List
from typing import Dict


def greedy_party(adj_matrix: List[List[int]], conv_list: List[int]) -> list[int]:
    number_employees: int = len(adj_matrix)

    invited: list = [0] * number_employees
    blocked: list = [False] * number_employees

    supervi: Dict[int, List[int]] = {i: [] for i in range(number_employees)}
    subordin: Dict[int, List[int]] = {i: [] for i in range(number_employees)}

    for i in range(number_employees):
        for j in range(number_employees):
            if adj_matrix[i][j] == 1:
                subordin[i].append(j)
                supervi[j].append(i)

    order: list = sorted(range(number_employees), key=lambda i: conv_list[i], reverse=True)

    for i in order:
        if not blocked[i] and all(invited[sup] == 0 for sup in supervi[i]) and all(invited[sub] == 0 for sub in subordin[i]):
            invited[i] = 1
            blocked[i] = True
            for n in supervi[i] + subordin[i]:
                blocked[n] = True

    conv_total: int = sum(conv_list[i] for i in range(number_employees) if invited[i] == 1)
    return invited + [conv_total]
