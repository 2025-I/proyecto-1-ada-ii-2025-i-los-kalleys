from tests.repetition import TestRepetition
from src.party.dinamic_solution import max_dinamic_invite_values
from src.utils.generate_tree import generate_tree_solution


class TestMaxDynamicPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_dinamic_invite_values, generate_tree_solution, lambda expected, result: self.assertListEqual(expected, result))

    def test_dynamic_solution(self):
        print("\nTiempos de ejecución de solucion dinamica party")
        self.run_all_tests([100, 1000, 10000])
