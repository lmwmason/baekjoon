c,n = map(int,input().split())
cost_list = [list(map(int,input().split())) for _ in range(n)]
dp = [100000000000000000000000000000000000000000000000000000000000000000007 for _ in range(1111)]
dp[0]=0

for i, j in cost_list:
    for k in range(j,c+100):
        dp[k] = min(dp[k-j]+i,dp[k])

print(min(dp[c:]))