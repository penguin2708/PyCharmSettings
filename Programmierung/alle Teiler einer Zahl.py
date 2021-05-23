# Zweck:    Berechne alle Teiler einer Liste von Zahlen
# Status:   prod
# Stand:    18.12.2020

def teiler(liste):
    """Berechne die Teiler einer Liste von ganzen Zahlen"""
    ergebnis = []
    for elem in liste:
        # print(elem)
        i = 1
        liste_teiler = []
        liste_zahl_teiler = []
        while i <= elem:
            if elem % i == 0:
                # print(i)
                liste_teiler.append(i)
            i += 1
        liste_zahl_teiler.extend((elem, liste_teiler))
        # extend erlaubt das Hinzufügen mehrerer Elemente
        ergebnis.append(liste_zahl_teiler)
    return ergebnis


liste_zahlen = [x for x in range(0, 1001)]
print(liste_zahlen)
x = teiler(liste_zahlen)

for elem in x:
    print(elem)

x = teiler([448])

zahlen = [448, 462]
print(teiler(zahlen))
