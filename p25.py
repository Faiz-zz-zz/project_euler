fib = 2
fib_prev = 1
n = 2
while len(str(fib)) < 1000:
    print(n)
    fib, fib_prev = fib + fib_prev, fib
    n += 1

print(n, fib, len(str(fib)))
