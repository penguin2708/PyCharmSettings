# Zweck:    Erzeuge alle Permutationen für alle Elemente eines Strings
# Status:   prod
# Stand:    18.12.2020
from itertools import permutations


def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            # print('e: ', e)
            for i in range(len(e) + 1):
                # print('perms: ', perms)
                # print('e[:i]: ', e[:i])
                # print('s[-1]: ', s[-1])
                # print('e[i:]: ', e[i:])
                perms.append(e[:i] + s[-1] + e[i:])
        return perms


print(permutations('abcdefg'))
print(len(permutations('abcdefg')))

input = '1234567890ABCDEF'
liste_input = list(input)
a = [x for x in input]
print(len(input))

print(len(permutations(input)))

# A Python program to print all
# permutations using library function

###########################################################################################
# Get all permutations of [1, 2, 3]
perm = permutations(a)
print(list(perm))
# Print the obtained permutations
for i in list(perm):
    print(i)
