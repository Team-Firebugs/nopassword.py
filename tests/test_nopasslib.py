import sys
sys.path.append("..")
import nopassword
import string

alphabet = string.letters + string.digits
seed = "abc123"
length = 64

length1 = 64
length2 = 63
token1 = nopassword.transform(seed=seed, alphabet=alphabet, length=length1)
token2 = nopassword.transform(seed=seed, alphabet=alphabet, length=length2)
print
print "Length - Transform"
print token1, length1, len(token1)
print token2, length2, len(token2)
assert len(token1) == length1
assert len(token2) == length2


seed1 = "abc123"
seed2 = "abc1234"
token1 = nopassword.transform(seed1, alphabet, length)
token2 = nopassword.transform(seed2, alphabet, length)
print
print "Diffrent seeds - Transform"
print token1, seed1
print token2, seed2
assert token1 != token2


print 
print "Alphabet - Transform"
alphabet1 = string.digits
alphabet2 = string.letters
token1 = nopassword.transform(seed, alphabet1, length)
token2 = nopassword.transform(seed, alphabet2, length)
print token1, alphabet1, seed
print token2, alphabet2, seed
assert token1 != token2 

print
print "Itterations - Generate"
itterations1 = 137
itterations2 = 101
token1 = nopassword.generate(seed, alphabet, length, itterations1)
token2 = nopassword.generate(seed, alphabet, length, itterations2)
print token1, itterations1
print token2, itterations2
