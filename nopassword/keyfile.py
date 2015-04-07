import os
import string


def crange(c1, c2):
    return "".join([chr(x) for x in range(ord(c1), ord(c2) + 1)])


def get_runes():
    r = {
        "alphanumeric": string.letters + string.digits,
        "large": crange("!", "~"),
        "digits": string.digits,
    }
    return r


def generate_alphabet(runes, length):
    result = ""
    space = int(255 / len(runes)) * len(runes)
    while len(result) < length:
        r = ord(os.urandom(1))
        if r > space:
            continue
        result += runes[r % len(runes)]
    return result
