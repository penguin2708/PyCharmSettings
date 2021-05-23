

liste = '123456890'
print('liste[:1] ', liste[:1])
print('liste[1:] ', liste[1:])
print('liste[1] ', liste[1])
print(liste[:-1])
print(liste[-1])
print(liste[-1:])
print(liste[0:1])
print(liste[1:3])
print(liste[:])
print(liste[-3])
print(liste[:-4])
print(liste[1:-1])

for e in liste[:-1]:
    print(e)
    print('len(e): ', len(e))
    for i in range(len(e) + 1):
        print('i: ', i)









# using time module
import time

# ts stores the time in seconds
ts = time.time()

# print the current timestamp
print(ts)

# using datetime module
import datetime;

# ct stores current time
ct = datetime.datetime.now()
print("current time: ", ct)
