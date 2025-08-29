def fib(p):
    a, b = [1,0], [0,1]
    for _ in range(p):
        a[0], b[0] = b[0], (a[0] + b[0])
        a[1], b[1] = b[1], (a[1] + b[1])
    return a
in_ = fib(int(input()))
print(*in_)