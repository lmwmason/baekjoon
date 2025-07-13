def fib(n):
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, (a + b) % 1000000000
    return a

in_ = int(input())

if in_ == 0:
    print(0)
    print(0)
else:
    f = fib(in_)
    sign = 1 if in_ > 0 else (-1 if (in_ % 2 == 0) else 1)
    print(sign)
    print(f)