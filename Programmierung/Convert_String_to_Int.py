# Zweck:    Konvertierung String to base64 to hex to int
# Stand:    prod
# Status:   28.12.2020

# import base64
from base64 import b64encode

s = b'Beispieltext'
# Using base64.b64encode() method
# string to base64
gfg = b64encode(s)

print(gfg)

# base64 to hexadezimal
hex = gfg.hex()
print(hex)

# hex to dec
i = int(hex, 16)
print(i)
