from tests.repetition import TestRepetition
from src.party.brute_force_solution import brute_force_party
from src.utils.generate_tree import generate_tree_solution


class TestBruteForcePalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(brute_force_party, generate_tree_solution, self.validate)

    def validate(self, size: int):
        def validate_aux(expected, result):
            if size > 10 and not expected:
                return None

            self.assertListEqual(expected, result)

        return validate_aux

    def test_toy(self):
        self.run_n_repetitions(10, 1)

    def test_brute_force_solution(self):
        print("\nTiempos de ejecución de fuerza bruta party")
