N, K = map(int, input().split())
WV = list()
dp = [[0 for _ in range((K + 1))] for _ in range(N + 1)]

for _ in range(N) :
    WV.append(list(map(int, input().split())))

for i in range(1, N+1):
    w, v = WV[i-1]
    for j in range(1, K+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])