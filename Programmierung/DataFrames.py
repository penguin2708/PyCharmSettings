import pandas as pd
import numpy as np
import random
import string
from datetime import datetime

# Creating an empty Dataframe with column names only
dfObj = pd.DataFrame(columns=['Datei', 'FileSize'])

print("Empty Dataframe ", dfObj, sep='\n')
print("Empty Dataframe ", dfObj)

f3 = 'f3'
size = 99787
# Append rows in Empty Dataframe by adding dictionaries
dfObj = dfObj.append({'Datei': 'f1', 'FileSize': 222}, ignore_index=True)
dfObj = dfObj.append({'Datei': 'f2', 'FileSize': 23333}, ignore_index=True)
dfObj = dfObj.append({'Datei': f3, 'FileSize': size}, ignore_index=True)
dfObj = dfObj.append({'Datei': f3, 'FileSize': size + 5555}, ignore_index=True)

print("Dataframe Contens ", dfObj, sep='\n')

# Zeile hinzufügen
d1 = {'col1': [1, 4, 3, 4, 5],
      'col2': [4, 5, 6, 7, 8],
      'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d1)
print("Original DataFrame")
print(df)

print('After add one row:')
d2 = {'col1': 10,
      'col2': 11,
      'col3': 12}
df = df.append(d2, ignore_index=True)
print(df)

# Spalten umbenennen:
df.rename(columns=({'col1': 'Spalte1', 'col2': 'Spalte2', 'col3': 'Spalte3'}), inplace=True)
print(df)
#
#
#
# Spalten hinzufügen
testdata = {'UID': ['840001003', '840054776', '840099876', '889799876'],
            'State': ['Alabama', 'Texas', 'Unassigned', 'Colorado'],
            'County': ['Out of AL', 'Out of TX', '', 'Jackson']}
df_testdata = pd.DataFrame(data=testdata)
print(df_testdata)

#
#
# Liste der Spaltennamen
cols = list(df_testdata.columns)
print(cols)

# berechnete Spalte hinzufügen - Substring
print(df_testdata['UID'].str[4:6])
df_testdata['UID2'] = df_testdata['UID'].str[4:6]

# if-condition
df_testdata['Flag11'] = df_testdata['State'].apply(lambda x: 'True' if 'Unassigned' in x else 'False')
df_testdata['Flag12'] = ''
df_testdata.loc[
    (df_testdata['State'].str.contains('Unassigned')) | (df_testdata['County'].str.contains('Out of')), ['Flag12']
] = 'yes'


# Nutzung einer Funktion zum Umkodieren von Werten


def group_state(series):
    if 'NY' in series:
        return 'NY'
    elif 'AL' in series:
        return 'AL'
    elif 'NJ' in series:
        return 'NJ'


df_testdata['Code'] = df_testdata['County'].apply(group_state)

#
#
#
df1 = pd.DataFrame()

df1['A'] = range(10)  # Werte von 0 bis inclusive 9
df1['B'] = range(11, 21, 1)  # Werte von 11 bis inclusive 20, Schrittweite = 1
df1['C'] = range(20, 10, -1)
df1['Code1'] = ''
df1['Code2'] = ''
df1['Code3'] = ''
df1['Code4'] = ''
df1['Code1'][df1['A'] > 2] = '>2'  # nicht empfehlenswert ! Code erzeugt eine Kopie des Slices ???
print(df1)
df1.loc[df1['A'] > 2, ['Code2']] = 'größer 2'
df1['Code3'][
    (df1['A'] > 2) & (df1['A'] < 4)] = '>2 und < 4'  # nicht empfehlenswert ! Code erzeugt eine Kopie des Slices ???
df1.loc[(df1['A'] > 2) & (df1['A'] < 4), ['Code4']] = 'zwischen 2 und 4'  # besserer Ansatz

#
#
#
# NUMPY- Examples/ see "Python Data Science Handbook"
np.random.seed(88)
x1 = np.random.randint(0, 100, size=10)
print("x1: ", x1)

x3 = np.random.randint(0, 100, size=(3, 4, 5))
print("x3: ", x3)
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 shape - 2.Dimension: ", x3.shape[1])
print("x3 size: ", x3.size)
print("x3 dtype: ", x3.dtype)
print("x3 itemsize in bytes: ", x3.itemsize)
print("x3 nbytes: ", x3.nbytes)
#
#
# 1-dimensionales Array
print(x1)
print(x1[0:5])
print(x1[:5])
print(x1[:-5])  # wie x1[:5]
print(x1[3:5])
print(x1[::2])  # jedes zweite Element
print(x1[::5])  # jedes fünfte Element
print(x1[4::2])  # jedes zweite Element, Start bei Index = 4
print(x1[::-1])  # negative Schrittweite ==> Ausgabe rückwärts alle Elemente
print(x1[3::-1])  # Start beim vierten Element (Index = 3) und Ausgabe rückwärts alle Elemente
#
#
#

# 2-dimensionales Array
x2 = np.random.randint(0, 100, size=(5, 10))  # 5 Zeilen, 10 Spalten
print(x2)
print(x2[:, 0])  # Spalte 1, alle Zeilen
print(x2[:, 3])  # Spalte 4, alle Zeilen
print(x2[:, 2:4])  # Spalten 3 bis 4, alle Zeilen
print(x2[:, 4::-1])  # Start beim fünften Element, ab da Spalten rückwärts, alle Zeilen
print(x2[::-1, ::-1])  # Spalten und Zeilen rückwärts
print(x2[0, :])  # erste Reihe
print(x2[1, :])  # zweite Reihe
print(x2[1])  # zweite Reihe
print(x2[:, 3])  # vierte Spalte. Ausgabe als Liste !!
#
#
#
# Data Indexing and Selection/ Kapitel 3 (Daten Manipulation with Pandas) aus: Python Data Science Data Handbook
# Name des Dictionary ==> column label; key ==> row labels; value ==> Werte
area = pd.Series({'California': 423967,
                  'Texas': 695662,
                  'New York': 141297,
                  'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521,
                 'Texas': 26448193,
                 'New York': 19651127,
                 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
print(data)

# Namen der Spalten ausgeben
print(data.columns)

data
data['area']
data.area
data.area is data['area']
data.values
data.values[0]  # Reihe 1
data['area']  # Spalte 1 incl. Row-Label
data.values[:, 0]  # Spalte 1 als Liste ohne Row-Label

# DataFrame transponieren
data_transposed = data.T

data['density'] = data['pop'] / data['area']
print(data)

s1 = data.iloc[:, 0]  # alle Zeilen, Spalte 1
s2 = data['area']
s3 = data.area
liste = [s1, s2, s3]
for element in liste:
    print(type(element))

s1 is s2  # ==> FALSE / WARUM?????
s2 is s3  # ==> TRUE
s1 is s3  # ==> FALSE

data.iloc[:3, :2]
data.loc[:'New York', :'pop']
data.iloc[0]
data.iloc[0, :]
data.iloc[2, 0]  # Zeile 3, Spalte 1

# hybride Selektion - 1. Wert der Spalte density
print(data.iloc[0, data.columns.get_loc('density')])
# oder eine offenbar schnellere Lösung
print(data.at[data.index[0], 'density'])

# gesamte Spalte ausgeben
print(data['density'])

# data['Florida', 'density']  # fehlerhaft
# data['Florida']  # fehlerhaft
# data['Florida', :]  # fehlerhaft

data.loc[data['density'] < 100]
data.loc[data['density'] < 100, ['pop',
                                 'area']]  # Spalten 'pop', 'area' (Reihenfolge) für alle Zeile mit einer bestimmten density

data.loc['California', :]  # alle Spalten für die Zeile 'California

data['flag1'] = ''  # neue Spalte erzeugen
data.loc[data['density'] < 100, ['flag1']] = 'Dichte < 100'
#

# Liste aller Spalten im DataFrame
print(data.head)
print(data.columns)  # Liste aller Spalten
#
i = 0
for element in data.columns:
    i += 1
    print(i, '   ', element)
#
#
#
# Spalten entfernen
data.drop(['area', 'density'], axis=1, inplace=True)

#
# *********************************************************************************************************************
# diverse Listen erzeugen

# category = ['A', 'B', 'C', 'D']
liste = ['A'] * 100 + ['B'] * 100 + ['C'] * 100 + ['D'] * 65  # Liste mit 365 Elementen
print(liste)
print(len(liste))



#
#
#
#
# Timeseries Data
# erzeuge jedes Datum zwischen start und ende.
df_dates = pd.date_range(start='1/1/2018', end='1/31/2018', freq='D')
cat = ['A', 'B', 'C']

type(df_dates)
print(df_dates)

# leerer Dataframe
df_timeseries_data = pd.DataFrame()

# Erzeuge für jedes Element aus der Liste 'cat' eine Zeitreihe mit Zufallszahlen
np.random.seed(99)
for c in cat:
    df_timeseries = pd.DataFrame(df_dates, columns=['Datum'])
    # Spalte 'category' erzeugen und mit konstantem Wert befüllen
    df_timeseries['category'] = c

    # Jede Zeile mit einem anderen Zufallswert befüllen
    df_timeseries['subcategory'] = [random.choice(['X', 'Y', 'Z']) for i in df_timeseries.index]

    # Das erste Element der Liste 'shape' (shape[0]) gibt die Anzahl der Zeilen des Dataframe zurück.
    # Der folgende Aufruf gibt shape[0] Werte zurück.
    df_timeseries['randNum'] = np.random.randint(10, 99, df_timeseries.shape[0])
    df_timeseries['lag1'] = 0
    df_timeseries['lag2'] = 0
    df_timeseries['lag3'] = 0
    df_timeseries['rownumber'] = 0

    #
    # Methode 1a:
    for i in range(0, len(df_timeseries)):
        print(i)

        # für die erste Zeile kann keine Differenz zum Vorgänger berechnet werden.
        if i == 0:
            df_timeseries.iloc[i, 4] = df_timeseries.iloc[i, 3]
        else:
            df_timeseries.iloc[i, 4] = df_timeseries.iloc[i, 3] - df_timeseries.iloc[i - 1, 3]

    # Methode 1b:
    for i in range(0, len(df_timeseries)):
        print(i)

        # für die erste Zeile kann keine Differenz zum Vorgänger berechnet werden.
        if i == 0:
            df_timeseries['lag3'].iloc[i] = df_timeseries['randNum'].iloc[i]
        else:
            df_timeseries['lag3'].iloc[i] = df_timeseries['randNum'].iloc[i] - \
                                            df_timeseries['randNum'].iloc[
                                                i - 1]
    # ACHTUNG. Append der Dataframes bewirkt, dass Zeilennummern mehrfach vorkommen (was durchaus gewollt sein kann!)
    df_timeseries_data = df_timeseries_data.append(df_timeseries)
#
#
#
print(list(df_timeseries_data.columns))
print(df_timeseries_data.shape)

# GROUPBY
grouped = df_timeseries_data.groupby('category')
for group in grouped:
    print(group)

# Berechne für jede Teilgruppe die Differenz der Spalte 'randNum' zur Vorgänger-Zeile und schreibe in
# die erste Zeile jeder Gruppe eine 0.
df_timeseries_data['lag0'] = df_timeseries_data.groupby('category')['randNum'].diff().fillna(0)

# Wert von 'randNum' in erster Zeile
print(df_timeseries_data.groupby('category')['randNum'].first())

# Zeilen je Gruppe von 1 - n durchnummerieren.
df_timeseries_data['rownumber'] = df_timeseries_data.groupby('category')['randNum'].cumcount() + 1

# Wert von 'rownumber' in Zeile 0
print(df_timeseries_data['rownumber'].iloc[0])


# Methode 2:
# Jeweils den ersten Wert von 'difference' durch 'randNum' ersetzen - Start
def test(df_x):
    df_x.at[df_x.index[0], 'lag0'] = df_x.at[df_x.index[0], 'randNum']
    return df_x


df_timeseries_data = df_timeseries_data.groupby('category').apply(test)
# Jeweils den ersten Wert von 'difference' durch 'randNum' ersetzen - Ende

print(list(df_timeseries_data.columns))


# Methode 3:
def berechne_differenz_zum_vorgaenger(df):
    for i in range(0, len(df)):
        print(i)

        # für die erste Zeile kann keine Differenz zum Vorgänger berechnet werden.
        if i == 0:
            df.iloc[i, 5] = df.iloc[i, 3]
        else:
            df.iloc[i, 5] = df.iloc[i, 3] - df.iloc[i - 1, 3]
    return df


df_timeseries_data = df_timeseries_data.groupby('category').apply(berechne_differenz_zum_vorgaenger)

# geht auch so, aber nur, wenn die Zeilen in jeder Gruppe von 1 bis n nummeriert sind.
berechne_differenz_zum_vorgaenger(df_timeseries_data)

## Berechnung von Statistiken für einen Dataframe mittels GROUPBY

df_new = df_timeseries_data.groupby('category').agg({'category': 'count', 'randNum': 'sum'}).rename(
    columns={'category': 'Anzahl Zeilen', 'randNum': 'Summe randNum'})

# ODER

df_new = (df_timeseries_data.groupby(['category', 'subcategory'])
          .agg({'category': 'count', 'randNum': 'sum'})
          .rename(columns={'category': 'Anzahl Zeilen', 'randNum': 'Summe randNum'}))

# BESSER:
df_new = (df_timeseries_data
          .groupby(['category', 'subcategory'])
          .agg({'category': 'size', 'randNum': 'sum'})
          .rename(columns={'category': 'Anzahl Zeilen', 'randNum': 'Summe randNum'})
          .reset_index())

df.groupby('group').agg(
    a_sum=('a', 'sum'),
    a_mean=('a', 'mean'),
    b_mean=('b', 'mean'),
    c_sum=('c', 'sum'),
    d_range=('d', lambda x: x.max() - x.min())
)

# ODER NOCH BESSER: named aggregations
df_new1 = (df_timeseries_data
           .groupby(['category', 'subcategory'])
           .agg(Anzahl_Zeilen1=('category', 'size'),
                Anzahl_Zeilen2=('category', 'count'),
                Summe_randNum=('randNum', 'sum'))
           .reset_index())

# List comprehension
liste1 = [3 * i % 5 for i in range(1, 21)]
df_liste1 = pd.DataFrame({'x': liste1})
print(df_liste1)
#
#
#