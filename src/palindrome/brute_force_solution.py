from utils.is_palindrome import is_palindrome


def max_subsequence_palindrome(text: str) -> str:
    longest_palindrome: str = ""
    text_length: int = len(text)

    for start in range(text_length):
        for end in range(start + 1, text_length + 1):
            substring: str = text[start:end]

            if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome
