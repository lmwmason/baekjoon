import sys
sys.setrecursionlimit(100001)

n = int(input())
graph = []
max_num = 0
ans = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for j in arr:
        if j > max_num:
            max_num = j

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] > h:
                visited[nx][ny] = 1
                dfs(nx, ny, h)

for h in range(max_num):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, h)
    ans = max(ans, cnt)

print(ans)
