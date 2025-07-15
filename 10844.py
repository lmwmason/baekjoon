n = int(input())

dp = list()
for i in range(1, n+2):
    dp.append([0,0,0,0,0,0,0,0,0,0,0])

dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][7] = 1
dp[1][8] = 1
dp[1][9] = 1

for i in range(2,n+1) :
    for j in range(0,10) :
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

sum_ = 0
print(sum(dp[n])%1000000000)