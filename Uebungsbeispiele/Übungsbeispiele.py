desk = "C:/Users/Work/Documents/Python/"
print(desk)
f = open(desk + "first.txt", "w")
f.write("this is my first file!")
f.write("hello world")
f.close()


f1 = open(desk + "first.txt", "a")
f1.write("\nGood Night!")
f1.close()


c = open('csvfile.csv','w')
c.write('hi there\n') #Give your csv text here.
## Python will convert \n to os.linesep
c.close()

c1 = open('csvfile.csv','a')
c1.write('2nd line\n')
c1.write('3rd line\n')
c1.close()

animals = ["cat", "bird", "horse", "tiger", "fish", "ele,phant", "fly", "lion"]
print(len(animals))
print(animals[0])
print(animals[7])
print(animals[2:5])
print(animals[5].find("e"))
