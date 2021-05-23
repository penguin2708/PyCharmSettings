import random
import string
import pandas as pd
import numpy as np

Zeilen = int(input("Wieviele Datensätze sollen erzeugt werden? "))
Wertebereich = list(string.ascii_uppercase)
sample1 = [random.choice(Wertebereich) for i in range(1, Zeilen + 1)]  # mit Zurücklegen

gruppe = ['A', 'B', 'C', 'D']
v1 = [random.choice(gruppe) for j in range(1, Zeilen + 1)]  # zufallsauswahl mit zurücklegen
print(v1)

v1 = [random.choice(gruppe) for i in range(1, Zeilen)]
v1_set = set(v1)  # liste in set wandeln
print(type(v1_set))
for x in v1_set:
    print(x)
v1_df = pd.DataFrame({'Group': v1})  # liste to dataframe

# normalverteilte Zufallszahlen mit Mittelwert 1 und Standardabweichung
v3_array = np.random.normal(0, 1, Zeilen - 1)
print(type(v3_array))  # numpy.ndarray
print('mean: ', np.mean(v3_array), '\n', 'standard deviation: ', np.std(v3_array))
v3 = v3_array.tolist()  # in Liste konvertieren
print(type(v3))

letters = string.ascii_uppercase
print(type(letters))
letters = list(letters)
print(type(letters))

# NUMPY- Examples/ see "Python Data Science Handbook"
np.random.seed(88)
x1 = np.random.randint(0, 100, size=10)
print("x1: ", x1)

# Zufallszahlen erzeugen
print(random.randint(0, 9))
# liste mit 20 Elementen
x = [random.randint(0, 9) for p in range(0, 10)] + [random.randint(0, 9) for p in range(0, 10)]
print(x)
