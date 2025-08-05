n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = min(a[0], 1)
dp[1][n-1] = min(a[n-1], 1)
for i in range(1, n):
    dp[0][i] = min(a[i], dp[0][i-1] + 1)
    dp[1][n-i-1] = min(a[n-i-1], dp[1][n-i] + 1)

ans = 0
for i in range(n):
    ans += min(dp[0][i], dp[1][i])

print(ans)