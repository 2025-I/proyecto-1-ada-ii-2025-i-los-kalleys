from palindrome.repetition import TestRepetition
from src.palindrome.dinamic_solution import max_dynamic_palindrome


class TestMaxDynamicPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_dynamic_palindrome)

    def test_dynamic_solution(self):
        print("\nTiempos de ejecución de solucion dinamica palindrome")
        self.run_all_tests()
