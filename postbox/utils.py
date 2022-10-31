import random

from english_words import english_words_lower_alpha_set


_random_words = tuple(english_words_lower_alpha_set)


def get_random_word() -> str:
    return random.choice(_random_words)


def get_random_postbox_id() -> str:
    return f"{get_random_word()}-{get_random_word()}{random.randint(1, 10)}"