import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[0 for _ in range(c+1)] for _ in range(m+1)] for _ in range(1<<n)]
visited = [[[False for _ in range(c+1)] for _ in range(m+1)] for _ in range(1<<n)]

stack = [(0, 0, c)]

while stack:
    nn, mm, cc = stack.pop()
    if visited[nn][mm][cc]:
        continue
    visited[nn][mm][cc] = True

    for i in range(n):
        if nn & (1 << i) or a[i] > c:
            continue
        if cc >= a[i]:
            nnn, nmm, ncc = nn | (1 << i), mm, cc - a[i]
            if not visited[nnn][nmm][ncc]:
                stack.append((nnn, nmm, ncc))
            if dp[nnn][nmm][ncc] < dp[nn][mm][cc] + 1:
                dp[nnn][nmm][ncc] = dp[nn][mm][cc] + 1
        else:
            if mm + 1 < m:
                nnn, nmm, ncc = nn, mm + 1, c
                if not visited[nnn][nmm][ncc]:
                    stack.append((nnn, nmm, ncc))
                if dp[nnn][nmm][ncc] < dp[nn][mm][cc]:
                    dp[nnn][nmm][ncc] = dp[nn][mm][cc]

ans = 0
for nn in range(1<<n):
    for mm in range(m):
        for cc in range(c+1):
            if ans < dp[nn][mm][cc]:
                ans = dp[nn][mm][cc]
print(ans)