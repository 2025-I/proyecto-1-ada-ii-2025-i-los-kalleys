from tests.repetition import TestRepetition
from src.palindrome.greedy_solution import greedy_palindromic_substring
from src.utils.generate_phrase import generate_test_phrase
from typing import Optional


class TestGreedyPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(greedy_palindromic_substring, generate_test_phrase, self.validate)

    def validate(self, _: Optional[int] = None):
        return self.assertIn

    def test_toy(self):
        self.run_n_repetitions(10, 1)

    def test_greedy_solution(self):
        print("\nTiempos de ejecución de solucion voraz palindrome")
        self.run_all_tests([100, 1000, 10000, 50000])
