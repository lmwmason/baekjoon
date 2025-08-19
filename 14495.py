def like_fib(p):
    a,b,c =1, 1, 1
    for _ in range(p-1):
        a, b, c=b, c, (a+c)
    return a

print(like_fib(int(input())))
