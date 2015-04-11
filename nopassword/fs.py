import os.path
import os
import stat

NP_DIR = os.path.join(os.path.expanduser("~"), ".nopassword")

def fs_load_keyfile(name):
    fname = os.path.join(NP_DIR, name+".json")
    if not os.path.isfile(fname):
        raise IOError("Keyfile not found")
    data = ""
    with open(fname, "r") as f:
        data = f.read()
    return data


def fs_store_keyfile(keyfile):
    try:
        os.makedirs(NP_DIR)
    except OSError:
        pass
    fname = os.path.join(NP_DIR, keyfile.data["name"]+".json")
    if os.path.isfile(fname):
        raise IOError("File exists")
    with open(fname, "w") as f:
        f.write(keyfile.dumps())
    os.chmod(fname, stat.S_IRUSR)

