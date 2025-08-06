def fib(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)


def get_fib_num(a,b) :
    cnt = 0
    i = 0
    while True :
        if fib(i) >= a and fib(i) <= b :
            cnt += 1
        if fib(i) > b :
            break
        i+=1
    return cnt

while True :
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        exit()
    print(get_fib_num(a, b))