"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

# stack = [(1, 1)]
#
# maxima = (1, 1)
# seen = set([])
# while stack:
#     new_stack = []
#     for item in stack:
#         num, depth = item
#         if num not in seen:
#             seen.add(num)
#             # print(item)
#             maxima = max([item, maxima], key=lambda k: (k[1], k[0]))
#             first = num * 2
#             second = (num - 1) / 3
#             if second == int(second) and second < 1000000 and second > 1:
#                 new_stack.append((second, depth + 1))
#             if first < 1000000 and first > 1:
#                 new_stack.append((first, depth + 1))
#     print(new_stack)
#     stack = new_stack
#
# print(maxima)


dic = {}

def rec(num, parent, depth):
    if num in dic:
        return depth + dic[num]
    if num == 1:
        dic[parent] = depth
        return depth
    else:
        if num % 2 == 0:
            return rec(num // 2, parent, depth + 1)
        else:
            return rec(num * 3 + 1, parent, depth + 1)


maxima = (0, 0)
for i in range(1, 1000000):
    val = (i, rec(i, i, 1))
    print(maxima[1], i, val)
    # print(dic)
    maxima = max([maxima, val], key=lambda k: k[1])

print(maxima)
