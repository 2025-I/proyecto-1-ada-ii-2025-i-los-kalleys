from src.palindrome.brute_force_solution import max_subsequence_palindrome
from tests.repetition import TestRepetition
from src.utils.generate_phrase import generate_test_phrase
from typing import Optional


class TestBruteForcePalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(
            max_subsequence_palindrome, generate_test_phrase, self.validate
        )

    def validate(self, _: Optional[int] = None):
        return self.assertIn

    def test_toy(self):
        self.run_n_repetitions(10, 1)

    def test_brute_force_solution(self):
        print("\nTiempos de ejecución de solucion fuerza bruta palindrome")
        self.run_all_tests([100, 1000])
