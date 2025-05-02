import re
import unicodedata


def normalizer(text: str) -> str:
    normalized: str = unicodedata.normalize('NFD', text)
    alphanumeric_only: str = re.sub(r'[^a-zA-Z0-9ñÑ]', '', normalized)

    return alphanumeric_only.lower()
