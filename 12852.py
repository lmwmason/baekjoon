n = int(input())

dp = [0 for _ in range(n+1)]
path = [[] for _ in range(n+1)]
path[1] = [1]

for i in range(2,n+1):
    dp[i], p = dp[i-1]+1, i-1
    if i%3 == 0 and dp[i//3]+1 < dp[i]:
        dp[i], p = dp[i//3]+1, i//3
    if i%2 == 0 and dp[i//2]+1 < dp[i]:
        dp[i], p = dp[i//2]+1, i//2
    path[i].append(i)
    path[i] += path[p]

print(dp[n])
print(*path[n])
