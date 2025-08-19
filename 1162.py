import sys
import heapq

inp = sys.stdin.readline
inf = 10**12

n, m, k = map(int, inp().split())
d = [[inf]*(n+1) for _ in range(k+1)]
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, inp().split())
    g[u].append((v, w))
    g[v].append((u, w))

for i in range(k+1): d[i][1] = 0
hq = [(0, 1, 0)]
while hq:
    cost, x, p = heapq.heappop(hq)
    if cost > d[p][x]:
        continue
    for y, w in g[x]:
        if d[p][y] > cost + w:
            d[p][y] = cost + w
            heapq.heappush(hq, (cost + w, y, p))
        if p < k and d[p+1][y] > cost:
            d[p+1][y] = cost
            heapq.heappush(hq, (cost, y, p+1))

print(min(d[i][n] for i in range(k+1)))
