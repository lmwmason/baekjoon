import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    dp[i][i + 1] = int(a[i] == a[i + 1])
for k in range(2, n):
    for i in range(n-k):
        j = i+k
        if a[i] == a[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(dp[x - 1][y - 1])
