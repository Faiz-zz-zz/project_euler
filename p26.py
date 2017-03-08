d = 1000


def recurring_numbers(num):
    solution_set = set([])
    curr_length = 0
    numerator = 1
    while numerator:
        while numerator < num:
            numerator *= 10

        if numerator in solution_set:
            return (num, curr_length)
        else:
            solution_set.add(numerator)

        numerator %= num

        curr_length += 1

    if not numerator:
        return (num, curr_length)




maxima = (0, 0)
for i in range(1, d + 1):
    curr = recurring_numbers(i)
    print(curr)
    maxima = max([maxima, recurring_numbers(i)], key=lambda k: k[1])

print(maxima[0])
