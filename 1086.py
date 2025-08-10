import sys, math
input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]
K = int(input().rstrip())

a = [x % K for x in data]
length = [len(str(x)) for x in data]
c = [pow(10, i, K) for i in range(1000)]

dp = [[-1 for _ in range(1 << n)] for _ in range(K)]

def dfs(k, b, l):
    global dp, a, c
    if dp[k][b] != -1:
        return
    dp[k][b] = 0
    if b == (1 << n) - 1:
        dp[k][b] = int(k == 0)
        return
    for i in range(n):
        if b & (1 << i):
            continue
        nk = (k + a[i] * c[l]) % K
        nb = b | (1 << i)
        dfs(nk, nb, l + length[i])
        dp[k][b] += dp[nk][nb]

dfs(0, 0, 0)

num, den = dp[0][0], math.factorial(n)
if not num:
    den = 1
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0 and den % i == 0:
            num //= i
            den //= i
    if num != 1 and den % num == 0:
        den //= num
        num = 1

print(num, '/', den, sep='')