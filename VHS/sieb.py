# last prime to print out
N = 400

# Liste initialisieren mit N-1 Elementen.
gestrichen = [False for x in range(2, (N + 1))]
# print(gestrichen[399])

print(gestrichen)

for i in range(0, N):
    if gestrichen[i]:
        del gestrichen[i]


for i in range(2, int((N + 1) ** 0.5)):
    if not gestrichen[i - 2]:
        print("i: ", i)

        for j in range(i * i, N - 1):
            print("j: ", j, "Wert: ", gestrichen[j])
            gestrichen[j - 2] = True

for k in range(int((N + 1) ** 0.5), N - 1):
    if not gestrichen[k - 2]:
        print("k: ", k)

for m, n in enumerate(gestrichen):
    print(m, n)
