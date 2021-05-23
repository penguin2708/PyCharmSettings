# import primefac # läuft derzeit nur unter Python 2.7
# help(primefac)
import decimal
import math
from collections import Counter
from decimal import *

getcontext()

getcontext().prec = 100
getcontext()

i = 966964919231535928923784038394217581040893952
i = 114017101443279264246592665073
i = 1000


# i_string = str(i)
# print(len(i_string))


# i_root = i ** 0.5
# print(int(i_root) ** 2)
# i_original = int(i_root ** 2)


def get_prime_factors(number):
    # number = Decimal(number)
    # ctx = Context()
    # create an empty list and later I will
    # run a for loop with range() function using the append() method to add elements to the list.
    counter = 1
    prime_factors = []

    # First get the number of two's that divide number
    # i.e the number of 2's that are in the factors
    while number % 2 == 0:
        prime_factors.append(2)
        number = number // 2
        counter += 1

    # After the above while loop, when number has been
    # divided by all the 2's - so the number must be odd at this point
    # Otherwise it would be perfectly divisible by 2 another time
    # so now that its odd I can skip 2 ( i = i + 2) for each increment
    # for i in range(3, int(math.sqrt(Decimal(number))) + 1, 2):
    for i in range(3, int(Decimal(number).sqrt()) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number // i
            counter += 1

            # Here is the crucial part.
            # First quick refreshment on the two key mathematical conjectures of Prime factorization of any non-Prime number
            # Which is - 1. If n is not a prime number AT-LEAST one Prime factor would be less than sqrt(n)
            # And - 2. If n is not a prime number - There can be AT-MOST 1 prime factor of n greater than sqrt(n).
            # Like 7 is a prime-factor for 14 which is greater than sqrt(14)
            # But if the above loop DOES NOT go beyond square root of the initial n.
            # Then how does that greater than sqrt(n) prime-factor
            # will be captured in my prime factorization function.
            # ANS to that is - in my first for-loop I am dividing n with the prime number if that prime is a factor of n.
            # Meaning, after this first for-loop gets executed completely, the adjusted initial n should become
            # either 1 or greater than 1
            # And if n has NOT become 1 after the previous for-loop, that means that
            # The remaining n is that prime factor which is greater that the square root of initial n.
            # And that's why in the next part of my algorithm, I need to check whether n becomes 1 or not,
    if number > 2:
        prime_factors.append(number)
        counter += 1

    prime_factors.extend(['counter', counter])

    return prime_factors


factors = (get_prime_factors(i))
Counter(factors)
print(len(factors))

check_i = (2 ** 167) * 11261543 * 474671137
print(check_i)
print(i - check_i)
print(factors)

print(list[1232, 2222])
