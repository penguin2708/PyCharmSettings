# Die Prozedur führt eine Caesar-Verschlüsselung auf einem Text aus.
# Das Quell-Alphabet schließt die Umlaute und ß mit ein. Alle anderen Zeichen werden nicht konvertiert.
# Das Alphabet ist sortiert. Der Quell-Text wird vor der Verschlüsselung in Großbuchstaben gewandelt.

# Creation-Date: 10.02.2019


# 1. Öffnen der Eingabedatei
with open("C:/Users/Work/Desktop/Python/juncker.txt", "r", encoding="utf-8") as input_file:
    klartext = input_file.read()

# klartext = "Abc. ß"

# Schlüssel
shift = input("Ganze Zahl >= 0 eingeben:  ")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß'
umfang_alphabet = len(alphabet)
# print("Altes Zeichen: ", alphabet[0], "Neues Zeichen: ", alphabet[0 + int(shift) % umfang_alphabet])


geheimtext = ""
for buchstabe in klartext:
    if buchstabe != 'ß':  # ß nicht in Großbuchstaben wandeln.
        buchstabe = buchstabe.upper()

    pos = alphabet.find(buchstabe)
    if pos != -1:  # Zeichen ist im Alphabet vorhanden.
        neu = alphabet[(pos + int(shift)) % umfang_alphabet]  # modulare Arithmetik
    else:
        neu = buchstabe

    geheimtext = geheimtext + neu

print(geheimtext)
