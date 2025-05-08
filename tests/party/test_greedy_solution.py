from tests.repetition import TestRepetition
from src.party.greedy_solution import greedy_party
from src.utils.generate_tree import generate_tree_solution, adj_matrix_greedy_solution
from typing import Optional


class TestGreedyParty(TestRepetition):
    def validate(self, size: Optional[int] = None):
        def validate_aux(expected, result):
            if size > 10 and not expected:
                self.assertEqual(size + 1, len(result))
                return None

            self.assertListEqual(expected, result)

        return validate_aux

    def test_toy(self):
        self.setAlgorithm(greedy_party, adj_matrix_greedy_solution, self.validate)

    def test_greedy_solution(self):
        print("\nTiempos de ejecución de solucion voraz party")
        self.setAlgorithm(greedy_party, generate_tree_solution, self.validate)
        self.run_all_tests([100, 1000, 10000])
