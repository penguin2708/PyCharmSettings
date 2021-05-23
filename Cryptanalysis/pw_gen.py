import string
import random
import pyzufall

print(string.ascii_letters)
print(string.hexdigits)

our_characters = string.ascii_letters + string.digits + string.punctuation
print(our_characters)

pw = ""
number_of_characters = len(our_characters)

for count in range(10):
    rnd_number = random.randint(0, number_of_characters)
    pw += our_characters[rnd_number - 1]

print(pw)

from pyzufall.generator import essen, beilage, trinken

s = "Heute Abend gibt es () mit () und dazu ein Glas ().".format(essen(), beilage(), trinken())
print(s)

from pyzufall.satz import satz

for i in range(1000):
    s = satz()
    print(s)
