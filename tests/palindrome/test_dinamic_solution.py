from tests.repetition import TestRepetition
from src.palindrome.dinamic_solution import max_dynamic_palindrome
from src.utils.generate_phrase import generate_test_phrase
from typing import Optional


class TestMaxDynamicPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_dynamic_palindrome, generate_test_phrase, self.validate)

    def validate(self, _: Optional[int] = None):
        return self.assertIn

    def test_toy(self):
        self.run_n_repetitions(10, 1)

    def test_dynamic_solution(self):
        print("\nTiempos de ejecución de solucion dinamica palindrome")
        self.run_all_tests([100, 1000, 10000])
