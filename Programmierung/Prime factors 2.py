import math


# return a dict or a list of primes up to N
# create full prime sieve for N=10^6 in 1 sec
def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = list(range(n + 1))
    sieve[1] = 0

    for i in range(2, nroot + 1):
        if sieve[i] != 0:
            m = int(n / i - i)
            sieve[i * i: n + 1:i] = [0] * (m + 1)

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None


i = 32535610350861218929402373343432584856134615644613646196
prime_sieve(i)

i = 1234567871625262534252617262516182726152627382726253425263837251692818189
print(i % 3)
