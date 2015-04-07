import hashlib

def transform(seed, alphabet, length):
    """Creates a sequence of letters from alphabet with specific length"""
    result = ""
    digest = hashlib.sha512(seed).digest()
    index = 0
    while len(result) < length:
        val = digest[len(result) % len(digest)]
        index += ord(val)
        result += alphabet[index % len(alphabet)]
    return result


def generate(seed, alphabet, length, itterations):
    """Generates a set of letters by itterating the transform"""
    seed = seed + alphabet
    result = ""
    for x in range(itterations):
        seed = result + seed
        result = transform(seed, alphabet, length)
    return result
