import pandas as pd

# df = pd.DataFrame()
# checklist = ['A', 'B', 'G', 'E']
# data = {'Row': [1, 2, 3, 4, 5, 6], 'Elements': ['D,B,A,T', 'D,C,F', 'D,A,F', 'H,Z', 'H,G', 'X,A']}
# df = pd.DataFrame(data)
# df['Intersection'] = df['Elements'].apply(lambda x: [ele for ele in x.split(",") if ele in checklist])


df = pd.DataFrame()
checklist = {'Group A': ['A', 'B', 'G', 'E'], 'Group B': ['C', 'Z']}
data = {'Row': [1, 2, 3, 4, 5, 6], 'Elements': ['D,B,A,T', 'D,C,F', 'D,A,F', 'H,Z', 'H,G', 'X,A']}
df = pd.DataFrame(data)
df['Intersection'] = df['Elements'].apply(lambda x: [ele for ele in x.split(",") if ele in checklist])

df['Intersection'] = [[] for _ in range(df.shape[0])]

for key, values in checklist.items():
    print(key)
    print(values)
    df['Intersection'] = df['Elements'].apply(lambda x: [ele for ele in x.split(",") if ele in values])
    df['Intersection'] = df.apply(
        lambda x: [ele for ele in x['elements'].split(",") if ele in values] if len(x['Intersection']) != 0 else x[
            'Intersection'])
    df['length'] = df['Elements'].apply(lambda x: len([ele for ele in x.split(",") if ele in values]))
    df['v1'] = df['length'].apply(lambda x: key if x > 0 else x)

# print('hello')
df['group'] = key
df['check'] = values

type(df['length'])
df['length'].dtype

# df.loc[, (df['length'] == 0)]['Mengenlehre'] = 'xxxxx'

checklist = ['A', 'B', 'G', 'E']
i = 0
for i in df.index:
    print(i)
    print(df.iloc[i, 1])
    df['loop'].iloc[i] = i
    df['test'].iloc[i] = df['Elements'].iloc[i].split(",")
    i += 1


    #df['Elements'].str.split(",", expand=False)

    print([ele for ele in df['loop'] if ele in checklist])
