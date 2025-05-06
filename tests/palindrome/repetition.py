import unittest
import time
from src.utils.generate_phrase import generate_list_test_phrase
from typing import Callable


class TestRepetition(unittest.TestCase):
    def setAlgorithm(self, algorithm: Callable[[str], str]):
        self._algorithm = algorithm

    def run_n_repetitions(self, num_tests: int, repetitions: int = 5):
        average_time: float = 0

        for _ in range(repetitions):
            list_phrase: list[tuple[str, str]] = generate_list_test_phrase(num_tests)
            start: float = time.time()
            self.run_multiple_tests(num_tests, list_phrase)
            end: float = time.time()
            average_time += end - start

        if repetitions == 1:
            return None

        print(
            f"Tiempo promedio de ejecución para tamaño {num_tests}: {average_time / repetitions:.4f} segundos"
        )

    def run_multiple_tests(self, num_tests: int, list_phrase: list[tuple[str, str]]):
        for i in range(num_tests):
            phrase, expected = list_phrase[i]
            result = self._algorithm(phrase)
            self.assertIn(expected, result)
