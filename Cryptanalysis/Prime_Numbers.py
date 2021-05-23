import sympy
import pandas as pd
import os

# inhalt = dir(sympy)
# for element in inhalt:
#     print(element)

prime_number = 1
numbers = []
# positions = [100000, 120000, 150000, 400000, 700000, 710000, 4]
positions = [1, 20, 9000, 100000]
for position in positions:
    number = sympy.prime(position)
    numbers.append(number)
    prime_number = prime_number * sympy.prime(position)

print(prime_number)

# prime_number = prime_number * (2 ** 127)
print(prime_number)

for j in range(1, 101):
    print(j, '. Primzahl: ', sympy.prime(j))


def primes(n):
    # erste n Primezahlen erzeugen
    PrimeNumbers = {'i': [i for i in range(1, n + 1)],
                    'prime': [sympy.prime(i) for i in range(1, n + 1)]}
    return pd.DataFrame(PrimeNumbers)


df = primes(1000)

path_out = r'C:\Users\Work\Desktop'

DataOut = os.path.join(path_out, 'Primes.xlsx')
with pd.ExcelWriter(DataOut) as writer:
    df.to_excel(writer, sheet_name='UID_ISO_FIPS', index=False, header=True)
