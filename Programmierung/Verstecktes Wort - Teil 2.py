import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os
import collections

# Arbeitsverzeichnis ermitteln
os.getcwd()


def distinct_count(liste):
    """Die Funktion zählt die Häufigkeiten der Elemente in einer Liste."""
    freq = []
    frequencies = {}
    for x in liste:
        if x not in freq:
            freq.append(x)
            frequencies[x] = 1
        else:
            for keys, values in frequencies.items():
                print(keys, values)
                if keys == x:
                    frequencies[x] += 1

    frequencies = collections.OrderedDict(sorted(frequencies.items()))
    return frequencies


chiffrat = 'YXXXXXXYYYXXXXYYYXYXXYXYYXXYYXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYXYXXXXYXXXYXXYXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXYYYYXXYYXXXXYYXYXXXXXXXXYYXXXXXXXYYYXXXXXXXXYYYYXXXXYYXXYYYYXXYYYYYYYYXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXYYYYYYYYYXXXXXXXYXXXXXXXYYYYYYXXYYYYYYXXYXXXXXXXYXXXXXXXYYYYYYYYYYYYYXXXYXXXXYXXYXXXXXYXYXXXXXYXYYXXXYXXYXYYYXXXYXXXXYYXYXXXXXXYYXXXXXXYXYXXXXYXXXYXXYXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXXXXXYYXXX'
chiffrat_liste = list(chiffrat)
print(distinct_count(chiffrat_liste))

# Chiffrat enthält insgesamt 448 Zeichen:
# die Teiler sind: [[448, [1, 2, 4, 7, 8, 14, 16, 28, 32, 56, 64, 112, 224, 448]]]

print(len(chiffrat))
chiffrat_liste = list(chiffrat)  # String in Liste umwandeln

# X und Y durch 0 bzw. 1 ersetzen.
new_list = []

i = 0
for x in chiffrat_liste:
    if x == 'X':
        new_list.append(0)
    else:
        new_list.append(1)
    i += 1

# 14 Elemente hinzufügen. Danach hat die Liste 448 + 14 = 462 Elemente.
# new_list.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


print(len(new_list))

# bitmap erzeugen.
# reshape (rows, columns)
#plt.imsave('bitmap_11x42_01.png', np.array(new_list).reshape(11, 42), cmap=cm.gray)
#plt.imsave('bitmap_14x32_01.png', np.array(new_list).reshape(14, 32), cmap=cm.gray)
plt.imsave('bitmap_14x32_01_A.png', np.array(new_list, order='A').reshape(14, 32), cmap=cm.gray)
plt.imsave('bitmap_32x14_01.png', np.array(new_list).reshape(32, 14), cmap=cm.gray)
plt.imsave('bitmap_28x16_01.png', np.array(new_list).reshape(28, 16), cmap=cm.gray)
plt.imsave('bitmap_16x28_01.png', np.array(new_list).reshape(16, 28), cmap=cm.gray)
#plt.imsave('bitmap_7x64_01.png', np.array(new_list).reshape(7, 64), cmap=cm.gray)
#plt.imsave('bitmap_8x56_01.png', np.array(new_list).reshape(8, 56), cmap=cm.gray)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_reshaped = np.array(test).reshape((3, 3), order='F')


array1 = np.array(new_list).reshape(28, 16)
for i in range(3):
    liste1 = np.rot90(array1).tolist()
    array = np.array(liste1).reshape(28, 16)
    print(array)



print(type(array1))
print(array1)
