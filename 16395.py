dp = [[0] * 31 for _ in range(31)]

for i in range(31):
    dp[i][0] = 1
    dp[i][i] = 1
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

n, k = map(int, input().split())
print(dp[n-1][k-1])