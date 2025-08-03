n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(n) :
    for j in range(100) :
        if j-L[i] >= 0 :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
        else :
            dp[i][j] = dp[i-1][j]

print(dp[n-1][99])