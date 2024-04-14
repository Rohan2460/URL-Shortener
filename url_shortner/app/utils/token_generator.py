import string
import random


def generate_token(size: int = 5) -> int:
    chars = string.ascii_letters + string.digits
    token = ""

    for i in range(size):
        token += random.choice(chars)

    return token


if __name__ == "__main__":
    print(generate_token())
