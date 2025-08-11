def fib(p):
    a, b = 0, 1
    for _ in range(p):
        a, b = b, (a + b)
    return a

print(fib(int(input())))