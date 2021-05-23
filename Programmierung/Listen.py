import os

cwd = os.getcwd()
print(cwd)

a = [[1, 2, 3], [4, 5, 6]]

print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 19
print(a[0])
print(b)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(len(a))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
        print(s)
print(s)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)

n = 3
m = 4
a = [0] * n
print(a)
for i in range(n):
    a[i] = [0] * m
print(a)

n = 3
m = 7
a = []
for i in range(n):
    a.append([0] * m)

n = 10
m = 2
a = [[0] * m for i in range(n)]

# -------------------------------------------------------------------------------
str = "C:/Users/Work/Documents/Eigenes Tableau-Repository"
root = "C:/Users/"
splitat = len(root)
l, r = str[:splitat], str[splitat:]

print(l)
print(r)

# -------------------------------------------------------------------------------


liste1 = ['A1', ['B1', 'B2']]
liste2 = ['A1', 'A2', 'A3']

# hierarchical list
liste3 = {'A1': ['B1', 'B2'], 'A2': ['B3', 'B4', 'B5'], 'A3': ['B6']}
for key, value in liste3.items():
    print(key)
    for elem in value:
        print(elem)

folder = {'PROJEKTE': ["U:/", "C:/Users/Work/OneDrive - Busch Analytics/PROJEKTE/"],
          'RESEARCH': ["W:/", "C:/Users/Work/OneDrive - Busch Analytics/RESEARCH/"],
          'DATEN': ["Y:/", "C:/Users/Work/OneDrive - Busch Analytics/DATEN/"],
          'PRIVAT': ["Z:/", "C:/Users/Work/OneDrive - Busch Analytics/PRIVAT/"]}
for key, value in folder.items():
    print(key)
    for elem in value:
        print(elem)

print(2 ** 2)  # Potenz
print(12 ^ 9)
print(13 % 2)  # Modulo
