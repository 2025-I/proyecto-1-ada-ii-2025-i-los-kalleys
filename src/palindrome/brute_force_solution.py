from itertools import combinations
from typing import Generator
import math

from utils.is_palindrome import is_palindrome


def calculate_max_length(n: int, max_combinations: int = 50000000000) -> int:
    for k in range(1, n):
        c = math.comb(n, k)

        if c >= max_combinations:
            return k

    return 5


def all_subsequences(text: str) -> Generator[str, None, None]:
    text_length: int = len(text)
    max_length: int = min(text_length, calculate_max_length(text_length))

    for length in range(max_length, 0, -1):
        for text_index in combinations(range(text_length), length):
            yield "".join(text[i] for i in text_index)


def max_subsequence_palindrome(text: str) -> str:
    longest_palindrome: str = ""

    for subseq in all_subsequences(text):
        if is_palindrome(subseq):
            longest_palindrome = subseq
            return longest_palindrome

    return longest_palindrome
