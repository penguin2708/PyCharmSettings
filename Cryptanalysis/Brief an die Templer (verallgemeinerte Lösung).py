import math

# chiffre = 'ABCDEFG1234567abcdefg'
# chiffre = 'BADCFE1G325476'
chiffre = 'CBAFED21G54376'

# Achtung! Templer-Files haben unterschiedliche encodings. (UTF-8, ISO-8859-1)
with open(
        r'C:\Users\Work\OneDrive - Busch Analytics\PRIVAT\Kryptographie\MysteryTwister\Brief an die Templer - Teil 3 '
        r'DE.txt',
        "r", encoding="'UTF8'") as input_file:
    chiffre = input_file.read()

print(chiffre)

len_plaintext = len(chiffre)
size_segment = 7
# rest = len_plaintext % size_segment
# number_segments = len_plaintext // size_segment
number_segments = math.ceil(len_plaintext / size_segment)


def permutations(space):
    if len(space) <= 1:
        return [space]
    else:
        perms = []
        for e in permutations(space[:-1]):
            for i in range(len(e) + 1):
                perms.append(e[:i] + space[-1] + e[i:])
        return perms


space = '1234567'
# print(permutations(space))

keys = permutations(space)


def decrypt_templer(chiffre, key):
    plaintext = ''
    start = 0
    for i in range(1, number_segments + 1):
        chunk = chiffre[size_segment * (i - 1): size_segment * i]
        start += size_segment
        print('chunk: ', chunk, 'size chunk: ', len(chunk))
        result = ''
        len_chunk = len(chunk)
        len_key = len(key)
        if len_chunk == len_key:
            for j in key[0:len_key]:
                # print(j)
                character = chunk[int(j) - 1]
                result = result + character
        else:
            key = remove_digits(key, len_chunk)
            for j in key[0:len_chunk]:
                print(j)
                character = chunk[int(j) - 1]
                result = result + character
        # print(result)
        plaintext = plaintext + result
    # print(plaintext)
    return (plaintext)


def check_result(chiffre, keys, keywords):
    i = 1
    for key in keys:
        print('Pass: ', i, '  Key: ', key)
        plaintext = decrypt_templer(chiffre, key)
        print('Plaintext: ', plaintext)
        check = any(ele in plaintext for ele in keywords)
        i += 1
        if check:
            return (key)


# test = '6574321'


def remove_digits(key, threshold):
    new_key = ''
    for c in key:
        if int(c) <= threshold:
            new_key = new_key + c
    return (new_key)


# print(remove_digits(test, 4))

keywords = ['Ritter', 'Templer', 'Kreuzzug', 'Jerusalem', 'Papst', 'Bruder', 'Brüder']
print('Der korrekte Schlüssel ist: ', check_result(chiffre, keys, keywords))

#################################


#
# print(chiffre[int('1')])
#

# test1 = ''

# print(test[-5:7])
# print([x for x in test if x >= 6])


# print(test[0:4])
# print(test[-2:4])
# print(test[-3:4])

# print(test[-2:])
# print(test[-2])
