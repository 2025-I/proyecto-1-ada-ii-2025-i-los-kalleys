from typing import Optional
import networkx as nx
import random


def generate_adj_matrix(size: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    matrix = [[0] * size for _ in range(size)]

    for origin, destination in edges:
        matrix[origin][destination] = 1

    return matrix


def generate_variable_tree(
    size: int, max_children: int = 2, seed: Optional[int] = None
) -> nx.Graph:
    if seed is not None:
        random.seed(seed)

    tree = nx.Graph()
    tree.add_node(0)

    next_node = 1
    cola = [0]

    while next_node < size and cola:
        random.shuffle(cola)
        parent = cola.pop(0)
        num_hijos = random.randint(1, min(max_children, size - next_node))

        for _ in range(num_hijos):
            if next_node >= size:
                break

            tree.add_edge(parent, next_node)
            cola.append(next_node)
            next_node += 1

    return tree


def generate_tree_solution(size: int) -> tuple[tuple[list[list[int], list[int]]], list[int]]:
    tree = generate_variable_tree(size)
    adj_matrix: list[list[int]] = generate_adj_matrix(size, list(tree.edges()))
    weights: list[int] = [random.randint(1, 50) for _ in range(size)]

    if size > 10:
        return ((adj_matrix, weights), [])

    complement_tree = nx.complement(tree)

    for node in complement_tree.nodes():
        complement_tree.nodes[node]["weight"] = weights[node]

    clique, total_sum = nx.max_weight_clique(complement_tree, weight="weight")
    best_independent_set = sorted(clique)
    nodes = [1 if node in best_independent_set else 0 for node in tree.nodes()]
    nodes.append(total_sum)

    return ((adj_matrix, weights), nodes)
