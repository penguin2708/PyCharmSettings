def convert_base(number, base):
    new_number = []
    while number > 1:
        number = number // base
        rest = number % base
        new_number.append(rest)
    return new_number


mersenne = 2 ** 127 - 1
zahl = convert_base(mersenne, 2)
print(len(zahl))

print(2 ** 10 - 1)
