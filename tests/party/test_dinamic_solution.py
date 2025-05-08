from tests.repetition import TestRepetition
from src.party.dinamic_solution import max_dinamic_invite_values
from src.utils.generate_tree import generate_tree_solution
from typing import Optional


class TestMaxDynamicPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_dinamic_invite_values, generate_tree_solution, self.validate)

    def validate(self, size: Optional[int] = None):
        def validate_aux(expected, result):
            if size > 10 and not expected:
                self.assertEqual(size + 1, len(result))
                return None

            self.assertListEqual(expected, result)

        return validate_aux

    def test_toy(self):
        self.run_n_repetitions(10, 1)

    def test_dynamic_solution(self):
        print("\nTiempos de ejecución de solucion dinamica party")
        self.run_all_tests([100, 1000, 10000])
