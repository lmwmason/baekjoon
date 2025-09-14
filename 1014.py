import sys
t = int(sys.stdin.readline())
ans = []

def dfs(x):
    global g, match, vis
    if vis[x]: return False
    vis[x] = True
    for y, link in enumerate(g[x]):
        if link:
            if y not in match or dfs(match[y]):
                match[y] = x
                return True
    return False

for _ in range(t):
    m, n = map(int, sys.stdin.readline().split())
    xs, ys = 0, 0
    match = {}
    cnt = 0
    seat = [[0]*n for _ in range(m)]
    X, Y = {}, {}
    g = [[0]*(n//2*m) for _ in range(((n+1)//2)*m)]
    for i in range(m):
        row = sys.stdin.readline().strip()
        turn = 0
        xi, yi = xs, ys
        for j, v in enumerate(row):
            if turn == 0:
                if v == ".": X[(i,j)] = (xi,1); cnt += 1
                else: X[(i,j)] = (xi,0)
                xi += m; turn = 1
            else:
                if v == ".": Y[(i,j)] = (yi,1); cnt += 1
                else: Y[(i,j)] = (yi,0)
                yi += m; turn = 0
        xs += 1; ys += 1
        for j, v in enumerate(row):
            if v == ".": seat[i][j] = 1
    for i,j in X:
        if not X[(i,j)][1]: continue
        for a,b in [(i-1,j-1),(i,j-1),(i+1,j-1),(i-1,j+1),(i,j+1),(i+1,j+1)]:
            if 0 <= a < m and 0 <= b < n and seat[a][b]:
                g[X[(i,j)][0]][Y[(a,b)][0]] = 1
    for i in range(len(X)):
        vis = [0]*len(X)
        dfs(i)
    ans.append(cnt - len(match))

for r in ans:
    sys.stdout.write(str(r)+'\n')
