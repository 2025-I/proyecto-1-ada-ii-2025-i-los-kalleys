from tests.palindrome.repetition import TestRepetition
from src.palindrome.greedy_solution import greedy_palindromic_substring


class TestGreedyPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(greedy_palindromic_substring)

    def test_greedy_solution(self):
        print("\nTiempos de ejecución de solucion voraz palindrome")
        self.run_all_tests()
