# Testdata

import random
import pandas as pd
import string

dir(string)

data = {'product': ['milk', 'butter', 'bread', 'beer', 'marmelade', 'apple'],
        'price': [1.20, 8.30, 0.25, 3.45, 1.25, 0.40]}
df_data = pd.DataFrame(data)

list(df_data)

r, c = df_data.shape
print('number of rows: ', r, 'number of columns: ', c)

print(df_data.shape[0])
print(df_data.shape[1])
print('name of columns: ', list(df_data.columns))

random.seed(400)
for i in range(10):
    print(i, random.normalvariate(0, 1))

## Buchstaben des Alphabets
alphabet = string.ascii_uppercase
type(alphabet)
print(alphabet[1])
i = 1
for letter in alphabet:
    print(i, letter, "\n", end='')
    i += 1

