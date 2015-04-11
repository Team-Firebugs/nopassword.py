import math
import sys
sys.path.append("..")
import nopassword

print
print "Predfined runes"
runes = nopassword.get_runes()
for k, v in runes.items():
    print k.ljust(20),  len(v),"\t", v


print 
print "Generate alphabets"
alphabets = {}
length = 5 
itterations = 0
rr = runes["digits"]
while True:
    itterations += 1
    alphabet = nopassword.generate_alphabet(runes = rr, length=length)
    if alphabet in alphabets:
        print "Duplicate after %d itterations" % itterations 
        print "Length:%d\tRunes:[%s]\t Possible permuations:%d\tPairs:%d" %( length, rr, len(rr)**length, itterations*(itterations-1))
        print sorted(alphabets.keys())
        break
    alphabets[alphabet] = True

