

"""Liest UTF-8 Dateien und gibt die Häufigkeit an


    input: filename
    outpute: stdout"""

import string

#1. Öffnen der Eingabedatei
with open("C:/Users/Work/Desktop/Python/Zeittafel.txt", "r", encoding="utf-8") as input_file:
    faust = input_file.read()

#2. Erzeugen einer Liste "words" aller Worte in Text
words = faust.split()
#3. Entfernen aller Satzzeichen aus den Worten
for index, word in enumerate(words):
    new_word = ""
    for char in word:
        if char not in string.punctuation:
            new_word += char
    words[index] = new_word

#4. Zählen jedes Wortes mittels Dictionary
word_count = dict()
for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

#5. Ausgabe der Ergebnisse
print(len(word_count))
for word in word_count.keys():
    print(word, ": ", word_count[word])
