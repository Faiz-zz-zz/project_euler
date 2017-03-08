UPPPER_LIMIT = 28123
# UPPPER_LIMIT = 30


divisors = {}


def find_divisors(n):
    for i in range(1, n + 1):
        # print("Finding divisors for " + str(i))
        for j in range(1, i // 2 + 1):
            if not i % j:
                if i in divisors:
                    divisors[i].add(j)
                else:
                    divisors[i] = set([j])


def filter_for_abundant():
    tbe = []
    for key, value in divisors.items():
        if sum(value) <= key:
            tbe.append(key)

    # filter them out of the dictionary
    for key in tbe:
        divisors.pop(key, None)


find_divisors(UPPPER_LIMIT)
filter_for_abundant()

abundants = list(divisors.keys())
possible_sums = [
                    abundants[i] + abundants[j] for i in range(len(abundants))
                    for j in range(len(abundants))
                    if (abundants[i] + abundants[j]) <= UPPPER_LIMIT
                ]

total = (UPPPER_LIMIT * (UPPPER_LIMIT + 1) / 2) - sum(set(possible_sums))
print("total = " + str(total))
