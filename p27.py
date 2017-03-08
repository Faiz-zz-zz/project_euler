import math

quad = lambda a, b, n: n ** 2 + a * n + b

primes = [2, 3]


prime_set = set([])


def sieve(num):
    hash = {i: True for i in range(1, num)}
    hash[1] = False

    for i in range(2, num):
        print(i)
        for j in range(2 * i, num, i):
            if hash[j]:
                hash[j] = False

    for i in range(1, num):
        if hash[i]:
            prime_set.add(i)

sieve(1000000)

max_found = (0, 0, 0)

for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        n = 0
        while quad(a, b, n) in prime_set:
            n += 1

        max_found = max([max_found, (a, b, n)], key=lambda k: k[2])
        if n:
            print(a, b, n)

print(max_found)
