n = int(input())
a = [list(map(int, input().strip())) for _ in range(n)]

d = dict()

def dfs(x, v, p):
    k = (x, tuple(v), p)
    if k in d:
        return d[k]
    r = 1
    for i in range(n):
        if not v[i] and a[x][i] >= p:
            v[i] = 1
            r = max(r, 1 + dfs(i, v, a[x][i]))
            v[i] = 0
    d[k] = r
    return r

v = [0] * n
v[0] = 1
print(dfs(0, v, 0))