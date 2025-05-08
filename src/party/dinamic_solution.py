from collections import defaultdict
import queue


def build_dependency_graph(matrix: list[list[int]]) -> tuple[dict[int, list[int]], list[int]]:
    num_emplyees: int = len(matrix)
    dependency_graph: dict[int, list[int]] = defaultdict(list)
    dependency_count: list[int] = [0] * num_emplyees

    for i in range(num_emplyees):
        for j in range(num_emplyees):
            if matrix[i][j] == 1:
                dependency_graph[i].append(j)
                dependency_count[j] += 1
    return dependency_graph, dependency_count


def topological_sort(dependency_graph: dict[int, list[int]], dependency_count: list[int], matrix) -> list[int]:
    cola: queue.Queue[int] = queue.Queue()
    topo_order: list[int] = []

    for i in range(len(matrix)):
        if dependency_count[i] == 0:
            cola.put(i)

    while not cola.empty():
        current_employee = cola.get()
        topo_order.append(current_employee)
        for subordinate in dependency_graph[current_employee]:
            cola.put(subordinate)

    return topo_order


def calculate_optimal_values(
        dependency_graph: dict[int, list[int]], values: list[int], topo_order: list[int]) -> dict[int, tuple[int, int]]:

    invitation_decisions: dict[int, tuple[int, int]] = {}
    for employee in reversed(topo_order):
        subordinates = dependency_graph[employee]

        invite_current = values[employee] + sum(invitation_decisions[subord][0] for subord in subordinates)
        skip_current = sum(max(invitation_decisions[subord][0], invitation_decisions[subord][1]) for subord in subordinates)

        invitation_decisions[employee] = (skip_current, invite_current)
    return invitation_decisions


def reconstruct_solution(
        dependency_graph: dict[int, list[int]], invitation_decisions: dict[int, tuple[int, int]],
        dependency_count: list[int], values: list[int]) -> list[int]:

    num_employees = len(dependency_count)
    result = [0] * num_employees

    def dfs(employee: int, invite: bool) -> None:
        if invite:
            result[employee] = 1
            for subordinate in dependency_graph[employee]:
                dfs(subordinate, False)
        else:
            result[employee] = 0
            for subordinate in dependency_graph[employee]:
                best_without, best_with = invitation_decisions[subordinate]
                dfs(subordinate, best_with > best_without)

    for i in range(num_employees):
        if dependency_count[i] == 0:
            best_without, best_with = invitation_decisions[i]
            dfs(i, best_with > best_without)

    suma = sum(values[i] for i in range(num_employees) if result[i] == 1)
    result.append(suma)
    return result


def max_dinamic_invite_values(matrix: list[list[int]], values: list[int]) -> list[int]:
    dependency_graph, dependency_count = build_dependency_graph(matrix)
    topo_order = topological_sort(dependency_graph, dependency_count[:], matrix)
    invitation_desicions = calculate_optimal_values(dependency_graph, values, topo_order)
    final_result = reconstruct_solution(dependency_graph, invitation_desicions, dependency_count, values)

    return final_result
