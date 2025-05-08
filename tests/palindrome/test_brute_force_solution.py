from src.palindrome.brute_force_solution import max_subsequence_palindrome
from tests.repetition import TestRepetition


class TestBruteForcePalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_subsequence_palindrome)

    def test_brute_force_solution(self):
        print("\nTiempos de ejecución de solucion fuerza bruta palindrome")
        self.run_all_tests()
