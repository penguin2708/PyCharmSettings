import datetime

a = 10
b = 20
c = 30

# Multiline 1
message = """{}: Start
{}: Dataframe hat {} Zeilen""".format(datetime.datetime.now(), datetime.datetime.now(), a)
print(message)

# Multiline 2
print('erste Zeile', 'zweite Zeile', 'dritte Zeile', sep='\n')


# Multiline 3
print('erste Zahl:  {}'.format(a), 'zweite Zahl: {}'.format(b), 'dritte Zahl: {}'.format(c), sep='\n')
