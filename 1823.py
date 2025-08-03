import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())

plant = list()
for i in range(n):
    plant.append(int(input()))

dp =[[0 for i in range(n)] for i in range(n)]
def max_get(a, b, c):
    if a==b : return c*plant[a]
    if dp[a][b] : return dp[a][b]

    dp[a][b] = max(max_get(a+1, b, c+1)+c*plant[a], max_get(a, b-1, c+1)+c*plant[b])
    return dp[a][b]

print(max_get(0, n-1, 1))