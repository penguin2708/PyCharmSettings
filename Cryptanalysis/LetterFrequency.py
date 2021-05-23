import string
from pandas import DataFrame
from pandas import ExcelWriter
from pathlib import Path
import os

import numpy as np
import matplotlib.pyplot as plt

# relative Buchstabenhäufigkeit in der deutschen Sprache ohne Unterscheidung in Klein/Großbuchstaben.
# Quelle: http://www1.ids-mannheim.de/fileadmin/kl/derewo/DeReChar-v-uni-030-b-l-2018-02-28-1.0.html

profil_german = {
    'a': '0,0601',
    'b': '0,0215',
    'c': '0,0269',
    'd': '0,0472',
    'e': '0,1601',
    'f': '0,0183',
    'g': '0,0306',
    'h': '0,0425',
    'i': '0,0775',
    'j': '0,003',
    'k': '0,0154',
    'l': '0,0379',
    'm': '0,028',
    'n': '0,0966',
    'o': '0,0268',
    'p': '0,0105',
    'q': '0,0003',
    'r': '0,0774',
    's': '0,0634',
    't': '0,0637',
    'u': '0,0382',
    'v': '0,0092',
    'w': '0,0143',
    'x': '0,0005',
    'y': '0,0011',
    'z': '0,0124',
    'ß': '0,0017',
    'ä': '0,0055',
    'ö': '0,0027',
    'ü': '0,0068'}

print(profil_german)

# 1. Öffnen der Eingabedatei
with open("C:/Users/Work/Desktop/Python/juncker.txt", "r", encoding="utf-8") as input_file:
    text = input_file.read()

# Alle Großbuchstaben in klein verwandeln.
text = text.lower()

# liste aller Klein-Buchstaben
lower = string.ascii_letters.lower()

# absolute Häufigkeit aller Kleinbuchstaben ermitteln.
counter = 0
letter_count = dict()
for letter in text:
    if letter in lower:
        counter += 1
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print("Der Text hat", counter, "Zeichen.")

# **************** relative Häufigkeit jedes Buchstabens berechnen. ***********************
# Dict in Liste umwandeln.
dict_liste = [[key, val] for key, val in letter_count.items()]  # Ergebnis ist eine Liste von Listen
print("dict_liste: ", dict_liste)
dict_liste_sortiert = sorted(dict_liste, key=lambda x: x[0])  # Sortiere nach dem ersten Element der jew. Teilliste.
print("dict_liste_sortiert: ", dict_liste_sortiert)

i = 0
for x in dict_liste_sortiert:
    share = x[1] / counter
    print(x)
    dict_liste_sortiert[i].append(share)
    i += 1

# **************** erzeuge dataframe **********************************
df = DataFrame(dict_liste)
df.columns = ["letter", "frequency", "share"]
df = df.sort_values(['letter'], ascending=[True])  # Dataframe sortieren.
print("df: ", df, "\nAnzahl Zeilen: ", len(df))

# ***************  Ausgabe nach Excel *********************************
# wenn Ausgabe-Datei bereits existiert, dann löschen.
my_file = Path("letters.xlsx")
if my_file.is_file():
    os.remove("letters.xlsx")
    print("Ausgabe-Datei existiert bereits und wird überschrieben.")

writer = ExcelWriter('letters.xlsx')
df.to_excel(writer, sheet_name='Buchstaben', index=False)
writer.save()

# ******************* BAR-CHART *****************************
buchstaben = df["letter"]
y_pos = range(len(df))
frequenz = df["share"]

plt.bar(y_pos, frequenz, align='center', alpha=0.5)
plt.xticks(y_pos, buchstaben)
plt.ylabel('')
plt.title('Häufigkeit der Buchstaben')
plt.show()
