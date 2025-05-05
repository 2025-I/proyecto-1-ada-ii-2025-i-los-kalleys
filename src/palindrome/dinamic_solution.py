def max_dynamic_palindrome(phrase: str) -> str:
    phrase_len: int = len(phrase)

    if phrase_len <= 1:
        return phrase

    max_length: int = 1
    start: int = 0
    matrix: list[list[bool]] = [[False for _ in range(phrase_len)] for _ in range(phrase_len)]

    def is_palindrome_range(i: int, j: int) -> bool:
        is_neighbor: bool = i + 1 == j

        if is_neighbor:
            return True

        return phrase[i] == phrase[j] and matrix[i + 1][j - 1]

    for i in range(phrase_len):
        matrix[i][i] = True

    for substr_len in range(2, phrase_len + 1):
        for i in range(phrase_len - substr_len + 1):
            j = i + substr_len - 1

            if is_palindrome_range(i, j):
                matrix[i][j] = True
                start = i
                max_length = substr_len

    end: int = start + max_length
    return phrase[start:end]
