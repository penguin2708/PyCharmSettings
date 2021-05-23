import Tools
import winsound
import time

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

winsound.Beep(400,200)

while True:
    message = input("Text eingeben: ")
    message = message.upper()

    if message == "":
        break
    morse_code = ""

    for char1 in message:
        if char1 in CODE.keys():
            morse_code = morse_code + CODE[char1]
        elif char1 == " ":
            morse_code = morse_code + " "

    print(morse_code)
            #print (CODE[char])

    for char2 in morse_code:
        if char2 == ".":
            winsound.Beep(300, 250)
        elif char2 == "-":
            winsound.Beep(300, 500)
        elif char2 == " ":
            time.sleep(1)
        time.sleep(0.1)
