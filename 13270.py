def solve(n) :
    fib = [1, 1]
    while True :
        fib.append(fib[-1] + fib[-2])
        if fib[-1] > n:
            break

    arr = []
    for i in range(1, len(fib) - 1):
        people = fib[i+1]
        chicken = fib[i]
        if people <= n:
            arr.append((people, chicken))

    dp_min = [99999999999] * (n+1)
    dp_max = [-99999999999] * (n+1)
    dp_min[0] = 0
    dp_max[0] = 0

    for i, j in arr:
        for k in range(i, n+1):
            dp_min[k] = min(dp_min[k], dp_min[k-i] + j)
            dp_max[k] = max(dp_max[k], dp_max[k-i] + j)
    return dp_min[n], dp_max[n]

a = int(input())
print(solve(a)[0], solve(a)[1])