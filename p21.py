"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
 each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
  and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def main(n):
    divisors = {}

    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            if not i % j:
                if i in divisors:
                    divisors[i].add(j)
                else:
                    divisors[i] = set([j])

    sum_map = {}
    for key, val in divisors.items():
        sum_map[key] = sum(val)

    total = 0

    for key in sum_map:
        if sum_map[key] in sum_map and key == sum_map[sum_map[key]]:
            print(key, sum_map[key])
            if key != sum_map[key]:
                total += (key + sum_map[key])
            sum_map[sum_map[key]] = -1
            sum_map[key] = -1
    print(total)

main(10000)
