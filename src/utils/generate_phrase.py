from faker import Faker
from normalize import normalizer
import random

fake = Faker()


def generate_random_palindrome(min_len: int = 20, max_len: int = 25) -> str:
    half_palindrome: str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(min_len, max_len) // 2))
    if random.choice([True, False]):
        return half_palindrome + half_palindrome[::-1]  # Palíndromo par
    else:
        return half_palindrome + random.choice('abcdefghijklmnopqrstuvwxyz') + half_palindrome[::-1]  # Palíndromo impar


def generate_test_phrase() -> tuple[str, str]:
    palindrome: str = generate_random_palindrome()
    length_phrase: int = random.randint(50, 60)

    base_text = fake.text(max_nb_chars=length_phrase * 2)[:length_phrase - len(palindrome)]

    clean_text: str = normalizer(base_text)
    insert_pos: int = random.randint(0, len(base_text))
    phrase: str = clean_text[:insert_pos] + palindrome + clean_text[insert_pos:]
    return phrase, palindrome
