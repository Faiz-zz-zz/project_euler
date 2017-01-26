def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

memo = {}
def memoize(fn, arg, memo):
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]
total = 0
for i in range(1, 34):
    fibm = memoize(fib,i, memo)
    if fibm%2 == 0:
        total += fibm
print total

