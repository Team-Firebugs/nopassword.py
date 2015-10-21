import json
import os

import os.path
import os
import stat
import random

NP_DIR = os.path.join(os.path.expanduser("~"), ".nopassword")

def fs_load_keyfile(name):
    fname = os.path.join(NP_DIR, name+".json")
    if not os.path.isfile(fname):
        raise IOError("Keyfile not found")
    data = ""
    with open(fname, "r") as f:
        data = f.read()
    return data


def store_keyfile(name,keyfile):
    try:
        os.makedirs(NP_DIR)
    except OSError:
        pass
    fname = os.path.join(NP_DIR, name+".json")
    if os.path.isfile(fname):
        raise IOError("File exists")
    with open(fname, "w") as f:
        f.write(json.dumps(keyfile))
    os.chmod(fname, stat.S_IRUSR)



def get_runes():
    import string

    def crange(c1, c2):
        return "".join([chr(x) for x in range(ord(c1), ord(c2) + 1)])

    r = {
        "alphanumeric": string.ascii_letters + string.digits,
        "ascii": crange("!", "~"),
        "digits": string.digits,
    }
    return r

def generate_keyfile():
    result = {}
    for k, v in get_runes().items():
        result[k] = generate_alphabet(v, 33337)
    return result

def generate_alphabet(runes, length):
    rnd = random.SystemRandom()
    return "".join([rnd.sample(runes, 1)[0] for x in range(length)])

def load_keyfile(name):
   keyfile = json.loads(fs_load_keyfile(name))
   return keyfile


