n, l, r = map(int, input().split())
dp = [[[0 for _ in range(r)] for _ in range(l)] for _ in range(n)]

dp[0][0][0] = 1

for i in range(n-1):
    for j in range(l):
        for k in range(r):
            if dp[i][j][k] > 0:
                if j+1 < l:
                    dp[i+1][j+1][k]+=dp[i][j][k]
                if k+1 < r:
                    dp[i+1][j][k+1]+=dp[i][j][k]
                dp[i+1][j][k]+=dp[i][j][k]*i

print(dp[n-1][l-1][r-1]%1000000007)