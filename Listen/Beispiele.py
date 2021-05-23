buchstaben_dict = {'z': 10, 'd': 8, 'a': 17, 'y': 9}
buchstaben_list = []
for i, j in buchstaben_dict.items():
    buchstaben_list.append((i, j))  # Ergebnis ist eine Liste von Tupeln.
print(buchstaben_list)
print(type(buchstaben_list[0]))


list_key_value = [[key, val] for key, val in buchstaben_dict.items()]  # Ergebnis ist eine Liste von Listen
print(list_key_value)

# jeden Wert aus list_key_value mit einer Zahl i multiplizieren und Ergebnis als drittes Element anhängen.
for x in list_key_value:
    print(x)
    x.append(x[1]*90)
    print(x)

print(list_key_value)  # Ergebnis: Der Inhalt von list_key_value wurde verändert.

# sortiere nach dem 2. Element in den Listenelementen.
print(sorted(list_key_value, key=lambda x: x[1], reverse=True))

######

sorted_buchstaben_dict_val = sorted(buchstaben_dict.items(), key=lambda x: x[1])  # sortiere nach value.
print(sorted(buchstaben_dict.items(), key=lambda x: x[1]))
print(sorted_buchstaben_dict_val)

for x in sorted_buchstaben_dict_val:
    print(x)


sorted_buchstaben_dict_key = sorted(buchstaben_dict.items())

for x in sorted_buchstaben_dict_key:
    print(x)