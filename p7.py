"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

primes = [2, 3, 5]
curr = 7
while len(primes) != 10001:
    if all(map(lambda k: curr % k != 0, primes)):
        primes.append(curr)
    curr += 2
    print(len(primes))

print(primes[-1])
