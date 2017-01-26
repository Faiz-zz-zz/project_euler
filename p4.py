max_found = 0

def pal(number):
    return str(number) == str(number)[::-1]

for i in range(100, 1000):
    for j in range(999, 99, -1):
        result = i * j
        if pal(result):
            max_found = max(max_found, result)


print(max_found)
