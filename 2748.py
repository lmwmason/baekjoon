def fib_ (n) :
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[-1]

while 1 :
    num = int(input())
    if num==-1 : break
    print(f"Hour {num}: {fib_(num)} cow(s) affected")