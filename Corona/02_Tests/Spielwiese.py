# für 02_Tests

import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

frames = [df1, df2, df3]

result1 = pd.concat(frames)
result2 = pd.concat(frames, keys=["x", "y", "z"])  # erzeugt hierarchical index !!
print(result2.loc["y"])

df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)

result3 = pd.concat([df1, df4], axis=1, keys=['df1', 'df4'])  # axis: 0 = index, 1 = columns
result4 = pd.concat([df1, df4], axis=0, keys=['df1', 'df4'])  # axis: 0 = index, 1 = columns/ default: axis = 0!
result3a = pd.concat([df1, df4], axis=1, join="inner")
result3b = pd.concat([df1, df4], axis=1, join="outer")
result3c = pd.concat([df1, df4], axis=1).reindex(df1.index)
result3d = pd.concat([df1, df4.reindex(df1.index)], axis=1)
result3e = pd.concat([df1, df4], axis=1).reindex(df4.index)
result4a = pd.concat([df1, df4], ignore_index=True, sort=False)
result4b = pd.concat([df1, df4], ignore_index=True, sort=True)

d = [["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

print("{:<8} {:<15} {:<10}".format('Name', 'Age', 'Percent'))

for v in d:
    name, age, perc = v
    print("{:<25} {:<15} {:<10}".format(name, age, perc))




#####################################################################################################
NaN = np.nan


def concat(columns):
    new_string = ''
    number_columns = len(columns)
    for elem in columns:
        if elem != '':
            new_string = new_string + elem + ','
    return new_string


concat(['', 'A', 'B', 'C'])


def concat1(col1, col2, col3):
    new_string = ''

    for elem in columns:
        if elem != '':
            new_string = new_string + elem + ','
    return new_string


print(list('b', 'v'))

print(df_global[['Province_State', 'Country_Region']])

print([str(i) for i in df_global[['Province_State', 'Country_Region']] if i])

df_test = pd.DataFrame({'Werte': ['a', 'b', 'c', np.nan, 'd', np.nan]})
df_test.fillna('m')

liste = ['a', 'b', 'c', '', 'd']
print(liste)
