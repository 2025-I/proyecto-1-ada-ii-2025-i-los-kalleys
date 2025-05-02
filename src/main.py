from utils.normalize import normalizer
from palindrome.brute_force_solution import max_subsequence_palindrome

if __name__ == "__main__":
    text = normalizer(
        "Llego a tierra y le dijo: Dabale arroz a la zorra el abad, ella aceptó"
    )
    print(max_subsequence_palindrome("radaroso"))
