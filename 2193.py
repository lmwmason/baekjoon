n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = dp[i-2]+dp[i-1]

print(dp[n-1])