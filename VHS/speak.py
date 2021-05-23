import sys
from win32com.client import constants
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SPVoice")
print("Type word or phrase, then Enter")
print("Ctrl+Z then enter to exit")
while True:
    try:
        s = input()
        speaker.Speak(s)
    except:
        if sys.exc_type is EOFError:
            sys.exit()
