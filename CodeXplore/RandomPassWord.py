# Project Random PassWord

import string
import random


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def password_generator(length=8):
    printable = f"{LETTERS},{NUMBERS},{PUNCTUATION}"
    printable = list(printable)

    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = "".join(random_password)

    return random_password


def length_password():
    length = input("How long do you your password: ")
    return int(length)


def main():
    password_length = length_password()
    password = password_generator(password_length)
    print(password)


if __name__ == "__main__":
    main()
