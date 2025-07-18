n = int(input())
wine_num = list()
for i in range(n) :
    wine_num.append(int(input()))

dp = [0 for _ in range(n+2)]

dp[0] = wine_num[0]

for i in range(1, n) :
    dp[i] = max(dp[i-1], wine_num[i]+wine_num[i-1]+dp[i-3], wine_num[i]+dp[i-2])

print(dp[-3])