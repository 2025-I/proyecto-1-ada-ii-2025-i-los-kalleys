def greedy_palindromic_substring(text: str) -> str:
    best: str = ""
    equal_count: int = 1

    def expand_center(current_i: int) -> str:
        right = current_i + 1
        left = current_i - equal_count

        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1

        return text[left + 1:right]

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            equal_count += 1
            continue
        candidate = expand_center(i)
        equal_count = 1

        best = max(best, candidate, key=len)

    return best
