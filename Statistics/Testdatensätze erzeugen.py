import random
import pandas as pd
import csv


# import os


def permutations(liste):
    """ Permutiere alle Elemente aus der Liste <elements>"""
    if len(liste) <= 1:
        return [liste]
    else:
        perms = []
        for e in permutations(liste[:-1]):
            for i in range(len(e) + 1):
                perms.append(e[:i] + liste[-1] + e[i:])
        return perms


elements = 'ABCDEFGH'
domain = permutations(elements)

j = 0
domain_numbered = []
for x in domain:
    j += 1
    domain_numbered.append([j, x])

seed = 23495561
n = 1 * (10 ** 2)
# zufall = random.choices(domain_numbered, k=n)  # ziehen mit zurücklegen
# # line = str(zufall)
#
# zufall = random.choices(domain_numbered, k=1)  # ziehen mit zurücklegen
# zufall[0].append(1)

# with open('testdata.csv', 'w') as outfile:
#     obj = csv.writer(outfile, delimiter=',')
#     obj.writerows(zufall)

# zufall = []
with open('testdata.csv', 'w', newline='') as outfile:
    obj = csv.writer(outfile, delimiter=';')
    for i in range(0, n):
        # zufall = []
        # test = []
        # test = random.choice(domain_numbered)  # ziehen mit zurücklegen
        # print(test)
        # print(random.choice(domain_numbered))
        # i = i + 1
        # test.append(i)
        # print(i)
        # print(test)
        obj.writerow(random.choice(domain_numbered))

zufall = random.choice(domain_numbered)


# the_file.write(line + '\n')
#
# df_testdata = pd.DataFrame(zufall)
# # df_testdata = pd.DataFrame(columns=['ID', 'Value'], dtype=)
#
# df_testdata.columns = ['ID', 'Value']
# zufall.clear()
#
# # os.getcwd()
# file = 'BigData.csv'
# df_testdata.index = df_testdata.index + 1
# df_testdata.to_csv(file, index_label='row')
