
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sieve(num):
    hash = {i: True for i in range(1, num)}
    hash[1] = False

    for i in range(2, num):
        for j in range(2 * i, num, i):
            if hash[j]:
                hash[j] = False

    total = 0
    for i in range(1, num):
        if hash[i]:
            total += i
            print(i)
    return total
print(sieve(2000001))
