
my_file = open("test.txt", "w")
for zahl in range(0, 1000000):
    if zahl % 100 == 0:
        print(zahl)
    my_file.write(str(zahl) + "\n")
my_file.close()
