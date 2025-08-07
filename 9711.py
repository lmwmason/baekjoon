def fib(p):
    a, b = 0, 1
    for _ in range(p):
        a, b = b, (a + b)
    return a

n = int(input())
for i in range(n):
    p, q = map(int, input().split())
    print(f"Case #{i+1}: {fib(p)%q}")