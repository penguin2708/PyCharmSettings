numbers_filename = "C:/Users/Work/Documents/Python/number.txt"
f = open(numbers_filename, "wt")
for i in range(10000000):
    f.write(str(i) + "\n")
f.close()