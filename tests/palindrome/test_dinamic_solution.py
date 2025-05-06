from palindrome.repetition import TestRepetition
from src.palindrome.dinamic_solution import max_dynamic_palindrome


class TestMaxDynamicPalindrome(TestRepetition):
    def setUp(self):
        self.setAlgorithm(max_dynamic_palindrome)

    def test_10(self):
        self.run_n_repetitions(10, 1)

    def test_100(self):
        self.run_n_repetitions(100)

    def test_1000(self):
        self.run_n_repetitions(1000)

    def test_10000(self):
        self.run_n_repetitions(10000)

    def test_50000(self):
        self.run_n_repetitions(50000)
