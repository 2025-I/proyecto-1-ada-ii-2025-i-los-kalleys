from itertools import combinations
from typing import FrozenSet


def build_graph(
    matrix: list[list[int]],
) -> set[FrozenSet[int]]:
    num_employees: int = len(matrix)
    invalid_pairs: set[FrozenSet[int]] = set()

    for supervisor in range(num_employees):
        for subordinate in range(num_employees):
            if matrix[supervisor][subordinate] == 1:
                invalid_pairs.add(frozenset((supervisor, subordinate)))

    return invalid_pairs


def is_valid_group(group: tuple[int, ...], invalid_pairs: set[FrozenSet[int]]) -> bool:
    selected: set[int] = set(group)
    for pair in invalid_pairs:
        if pair.issubset(selected):
            return False
    return True


def compute_total_compatibility(
    group: tuple[int, ...], compatibility: list[int]
) -> int:
    return sum(compatibility[i] for i in group)


def brute_force_party(matrix: list[list[int]], compatibility: list[int]) -> list[int]:
    compatibility_len: int = len(compatibility)
    invalid_pairs = build_graph(matrix)

    best_sum: int = 0
    best_group: list[int] = []

    for r in range(1, compatibility_len + 1):
        for group in combinations(range(compatibility_len), r):
            if not is_valid_group(group, invalid_pairs):
                continue

            current_sum: int = compute_total_compatibility(group, compatibility)

            if current_sum > best_sum:
                best_sum = current_sum
                best_group = list(group)

    selected_employees: list[int] = [
        1 if i in best_group else 0 for i in range(compatibility_len)
    ]
    selected_employees.append(best_sum)

    return selected_employees
