"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


curr = 2520

while curr:
    if all(map(lambda k: curr % k == 0, [i for i in range(1, 21)])):
        print(curr)
        exit()
    # print(curr)
    curr += 20
