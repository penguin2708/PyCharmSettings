import pandas as pd
import numpy as np

data = {'Name': ['James', 'Paul', 'Richards', 'Marico', 'Samantha', 'Ravi', 'Raghu', 'Richards', 'George', 'Ema',
                 'Samantha', 'Catherine'],
        'State': ['Alaska', 'California', 'Texas', 'North Carolina', 'California', 'Texas', 'Alaska', 'Texas',
                  'North Carolina', 'Alaska', 'California', 'Texas']}

df1 = pd.DataFrame(data, columns=['Name', 'State'])

print(df1)

#
# Häufigkeiten
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers,
# Python objects, etc.). The axis labels are collectively referred to as the index.
#
s1_freq = df1.State.value_counts()  # Schreibe Ergebnis in Serie.
print(s1_freq.index)  # gibt row-labels als Liste zurück
print(s1_freq.values)  # gibt Werte als Liste zurück

type(s1_freq)  # Series

# Umwandeln der Series in einen DataFrame mit benannten Spalten
df_freq = pd.DataFrame({'State': s1_freq.index, 'Frequency': s1_freq.values})
print(df_freq.loc[df_freq['Frequency'] >= 3])  # Gib alle Staaten mit Frequency >= 3 zurück.
