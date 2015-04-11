#!/usr/bin/env python
import sys

import argument
import pyperclip

import nopassword


def create_store_keyfile(name):
    keyfile = nopassword.generate_keyfile()
    try:
        nopassword.store_keyfile(name, keyfile)
    except IOError:
        print "Failed: Keyfile exists"
        sys.exit(3)
    return keyfile

runes = nopassword.get_runes()


f = argument.Arguments()
f.required("seed", help="Seed to generate password")
f.option("keyfile", "default", help="Keyfile to use", abbr="k")

f.option("alphabet", "ascii",
         help="Character set used: [%s]" % (", ".join(sorted(runes.keys()))),
         abbr="a"
         )
f.option("itterations", 113, help="Number of itterations", abbr="i")
f.option("length", 73, help="Length of generated passwords", abbr="l")

f.switch("help", help="Display options and commands", abbr="h")
f.switch("generate", help="Generate new keyfile", abbr="g")

f.process("length", lambda x: int(x))
f.process("itterations", lambda x: int(x))

f.validate("alphabet", lambda x: x in runes)

args, errors = f.parse()

if args["help"]:
    print f
    sys.exit(0)
if args["generate"]:
    create_store_keyfile(args["keyfile"])
    print "Keyfile %s created" % (args["keyfile"])
    sys.exit(0)

for e in errors:
    print e
    sys.exit(2)

try:
    keyfile = nopassword.load_keyfile(args["keyfile"])
except IOError:
    if args["keyfile"] == "default":
        print("No default keyfile found. Creating new")
        keyfile = create_store_keyfile("default")
    else:
        print("Failed: Keyfile [%s] not found" % (args["keyfile"]))
        sys.exit(2)

token = nopassword.generate(
    seed=args["seed"],
    alphabet=keyfile[args["alphabet"]],
    length=args["length"],
    itterations=args["itterations"]
)

pyperclip.copy(token)
print("Nopassword - Token in clipboard.")
