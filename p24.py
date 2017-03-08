array = [i for i in range(10)]

from itertools import permutations

perms = list(permutations(array))

other = []

for p in perms:
    other.append(int(''.join(list(map(str, p)))))

other.sort()

print(other[999999])
