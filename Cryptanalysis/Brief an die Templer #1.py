# 1. Öffnen der Eingabedatei
with open(
        r'C:\Users\Work\OneDrive - Busch Analytics\PRIVAT\Kryptographie\MysteryTwister\Brief an die Templer - Teil 1 '
        r'DE.txt',
        "r", encoding="'ISO-8859-1'") as input_file:
    chiffrat = input_file.read()

print(chiffrat)

# chiffrat = '1234567890ABC'
klartext = ''
n = 0
len_chiffrat = len(chiffrat)

for i in range(len_chiffrat):
    if (i + 1 == len_chiffrat) and (len_chiffrat % 2 != 0):
        klartext = klartext + chiffrat[i]
    else:
        n = i - 1 * ((-1) ** (i + 1))
        klartext = klartext + chiffrat[n]

print(klartext)

with open("myfile.txt", "w") as output_file:
    output_file.write(klartext)
