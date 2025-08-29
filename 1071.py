n = int(input())
num = list(map(int, input().split()))
dp = [0 for _ in range(1003)]
for x in num:
    dp[x] += 1

res = []
i = 0
while sum(dp) > 0:
    f = 1
    if dp[i] and dp[i+1]:
        for x in range(i+2, 1001):
            if dp[x]:
                res += [i]*dp[i]
                dp[i] = 0
                res.append(x)
                dp[x] -= 1
                f = 0
                break
        if f:
            res += [i+1]*dp[i+1]
            dp[i+1] = 0
            res += [i]*dp[i]
            dp[i] = 0
    else:
        res += [i]*dp[i]
        dp[i] = 0
    i += 1

print(*res)
