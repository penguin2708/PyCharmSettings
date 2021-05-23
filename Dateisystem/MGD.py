import os
import pandas as pd

infile = r'C:\Users\Work\Desktop\MGD\Impressions per year & month by requested_ad_size.csv'

MGD = {'InStream': ['10x1', '15x1', '20x1', '25x1', '40x1', '50x1', '480x360v', '480x361v', '640x480v'],
       'nativeVideo': ['11x1'],
       'SwitchIn': ['420x240']}
print(infile)

df_GAM = pd.read_csv(infile, sep=';')

# liste = '300x50,2x5,10x1,15x1,300x100,1010x250,970x250'
liste = '2x5,1x2,1x5,970x250'
liste1 = liste.split(",")
print(liste1)

# df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(lambda x: 1 if any(ele in ele for ele in liste.split(",")) else 0)
df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(
    lambda x: 1 if len([ele for ele in x.split(",") if ele in liste1]) > 0 else 0)
df_GAM['Liste'] = df_GAM['Requested ad sizes'].apply(lambda x: x.split(","))
df_GAM['Schnittmenge'].astype('object')
df_GAM['Schnittmenge'] = df_GAM['Requested ad sizes'].apply(lambda x: [ele for ele in x.split(",") if ele in liste1])
df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(lambda x: [ele for ele in x.split(",") if ele in liste1])
df_GAM['Flag1'] = df_GAM['Requested ad sizes'].apply(lambda x: x.contains('|'.join(liste1)))

s.str.contains('|'.join(l))

df['price'] = df.apply(lambda row: valuation_formula(row['x'], row['y']), axis=1)
df_GAM['Mengenlehre'] = df_GAM.apply(
    lambda row: [ele for ele in row['Requested ad sizes'].str.split(",", n=1) if ele in liste1], axis=1)

data["Team"] = data["Team"].str.split("t", n=1, expand=True)

df_GAM['Result'] = df_GAM['Requested ad sizes'].apply(lambda x: x in x.split(","), liste1)
type(df_GAM['Schnittmenge'])

[x
 for x in liste1 if x in liste3]

for key in MGD.keys():
    print(key)

for
    for key, value in MGD.items():
        if
res = [ele for ele in df_GAM[1] if (ele in '15x1, 300x1')]
print(key)

df_GAM['Flag'] = df_GAM.apply(
    lambda x: [x for x in df_GAM['Requested ad sizes'] if (x in '15x1, 300x1')], axis=1)

df_GAM['Flag'] = df_GAM.apply(
    lambda x: any(x in df_GAM['Requested ad sizes'] for x in ['10x1, 160x50']))

df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(lambda x: 1 if ['10x1, 160x50'] in x else 0)

print(df_GAM['Requested ad sizes'].dtype)
type(df_GAM['Requested ad sizes'])

df_GAM['Flag'] = df_GAM.apply(
    lambda x: '10x1' in x.values)

liste = '10x1, 15x1'
if '11' in liste:
    print('yes')
else:
    print('no')

if any(x in liste for x in ['9', '2', 'x']):
    print('yes')
else:
    print('no')

# ok
df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(lambda x: 1 if '10x1' in x else 0)

df_GAM['Flag'] = df_GAM['Requested ad sizes'].apply(lambda x: 1 if any(ele in x for ele in ['10x1', '160x50']) else 0)

res = any(ele in test_string for ele in test_list)

# initializing string
test_string = "There are 2 appless for 4 persons"

# initializing test list
test_list = ['apples', 'oranges']

# printing original string
print("The original string : " + test_string)

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# checking if string contains list element
res = any(ele in test_string for ele in test_list)

# print result
print("Does string contain any list element : " + str(res))

liste1 = ['10x1', '15x1', '300x100']
liste2 = ['710x1', '15x1', '310x100', '300x100', '15x11']
liste3 = ['11x1', '25x1', '310x100']

schnittmenge = [x for x in liste1 if x in liste2]
print(schnittmenge)
