import unittest
import time
from typing import Callable


class TestRepetition(unittest.TestCase):
    def setAlgorithm(self, algorithm: Callable[[str], str], generate_test: Callable, validate: Callable):
        self._algorithm = algorithm
        self._generate_test = generate_test
        self._validate = validate

    def run_n_repetitions(self, num_tests: int, repetitions: int = 5):
        average_time: float = 0

        for _ in range(repetitions):
            (entry, expected) = self._generate_test(num_tests)
            start: float = time.time()

            result = self._algorithm(*entry)

            end: float = time.time()

            self._validate(num_tests)(expected, result)
            average_time += end - start

        if repetitions == 1:
            return None

        print(
            f"Tiempo promedio de ejecución para tamaño {num_tests}: {average_time / repetitions:.4f} segundos"
        )

    def run_all_tests(self, sizes: list[int]):

        for size in sizes:
            self.run_n_repetitions(size)
