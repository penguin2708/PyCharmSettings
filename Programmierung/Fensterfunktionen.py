import random
import string
import numpy as np
import collections
import pandas as pd


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


def testdata_2dimensional(gruppen):
    """Diese Funktion erzeugt einen 2-dimensionalen Datensatz (Counter: i,j,k; Group, Subgroup, eine Wertespalte);
    Input ist eine Liste von Strings; Rückgabewert ist ein Dataframe."""

    df_testdata = pd.DataFrame(columns=['i', 'j', 'k', 'Group', 'Subgroup', 'Value'])

    # using dictionary to convert specific columns
    convert_dict = {'Value': float}  # float erlaubt NaN, integer nicht !
    df_testdata = df_testdata.astype(convert_dict)

    buchstaben = list(string.ascii_uppercase)

    ebene_1 = []
    ebene_2 = []
    i = 0
    k = 0

    for m in gruppe:
        anzahl = random.randint(2, 26)
        # max, wenn 'ohne zurücklegen' == 26 !
        sample = np.random.choice(buchstaben, replace=False, size=anzahl)  # ohne Zurücklegen
        i += 1
        j = 0  # beginnt bei jeder gruppe wieder von vorne
        for n in sample:
            j += 1
            k += 1
            ebene_1.append(m)
            ebene_2.append(n)
            wert = random.randint(0, 10)
            df_testdata.loc[k] = [i, j, k, m, n, wert]
            print(i, j, k, m, n, wert)

    return df_testdata


gruppe = ['A', 'B', 'C', 'D']
df = testdata_2dimensional(gruppe)
print(df.dtypes)
print(distinct_count(df['Subgroup']))

df_partition = testdata_2dimensional(gruppe)

# zwei Gruppen mit Subgroup = NULL einfügen.
df_test = pd.DataFrame({'Group': ['A', 'E'], 'Subgroup': ['', '']})
df_partition = df_partition.append(df_test, ignore_index=True)  # refresh index
df_partition = df_partition.sort_values(by=['Group', 'Subgroup'])
df_partition.index = df_partition.index + 1
print(df_partition.shape)
print(df_partition)

# Zähle Häufigkeit eines Elements
Subgroup_A = (df_partition.Subgroup == 'F').sum()  # True = 1
df_partition1 = df_partition.groupby('Group').count()  # Häufigkeiten für jede Spalte excl. der Gruppierungsvariable
df_partition2 = df_partition.groupby('Group').apply(lambda grp: (grp.Subgroup == 'F').sum())
df_partition3 = df_partition.groupby('Group').apply(lambda grp: grp.Subgroup.count() - (grp.Subgroup == 'F').sum())
print(df_partition.count())  # Klammern nach Count !!
print(len(df_partition.index))  # schnellste Methode zur Ermittlung der Zeilenanzahl

# Berechnung diverser Window-Funktionen (SQL-Äquivalent: OVER PARTITION BY)
df_partition['Mittelwert'] = df_partition.groupby('Group')['Value'].transform('mean')
# df_partition['Mittelwert'] = df_partition.groupby('Group').Value.transform('mean') # alternative Schreibweise
df_partition['Anzahl A'] = df_partition.groupby('Group').Subgroup.transform(lambda x: (x == 'G').sum())
df_partition['Anzahl NULL'] = df_partition.groupby('Group').Subgroup.transform(lambda x: (x == '').sum())
df_partition['Anzahl Datensätze'] = df_partition.groupby('Group').Group.transform(
    'count')  # Es muss genau ein Feld angegeben werden.
df_partition['Subgroup == NULL'] = df_partition['Subgroup'].apply(lambda x: 1 if x == '' else 0)

# Datenkonstellationen ermitteln.
for i in df_partition.index:

    # Fall1: Country hat genau eine Province/State; Diese hat den Wert NULL
    if df_partition.loc[i, 'Anzahl Datensätze'] == 1:
        df_partition.loc[i, 'Select'] = 'yes'

        # Fall2: Country hat mehr als eine Province/State; genau eine davon hat den Wert NULL
    elif df_partition.loc[i, 'Anzahl Datensätze'] > 1 and df_partition.loc[i, 'Anzahl NULL'] == 1 and df_partition.loc[
        i, 'Subgroup == NULL'] == 0:
        df_partition.loc[
            i, 'Select'] = 'no'

    elif df_partition.loc[i, 'Anzahl Datensätze'] > 1 and df_partition.loc[i, 'Anzahl NULL'] == 1 and df_partition.loc[
        i, 'Subgroup == NULL'] == 1:
        df_partition.loc[i, 'Select'] = 'yes'

    # Fall3: Country hat mehr als eine Province/State; keine davon hat den Wert NULL
    elif df_partition.loc[i, 'Anzahl Datensätze'] > 1 and df_partition.loc[i, 'Anzahl NULL'] == 0:
        df_partition.loc[
            i, 'Select'] = 'yes'
    else:
        print(i)
        df_partition.loc[i, 'Select'] = 'undefined'
