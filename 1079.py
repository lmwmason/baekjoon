n = int(input())
p = list(map(int, input().split()))
chg = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
is_survive = [1 for _ in range(n)]
ans = 0
stack = [(n, 0, p[:], is_survive[:])]

while stack:
    c, t, cur, s = stack.pop()
    ans = max(ans, t)
    if (c == 1 and s[m]) or not s[m]:
        continue
    if c % 2:
        mx, idx = -1e18, 0
        for i in range(n):
            if s[i] and cur[i] > mx:
                mx, idx = cur[i], i
        new_s = s[:]
        new_s[idx] = 0
        stack.append((c-1, t, cur[:], new_s))
    else:
        for i in range(n):
            if s[i] and i != m:
                new_cur, new_s = cur[:], s[:]
                new_s[i] = 0
                for j in range(n):
                    if j != i:
                        new_cur[j] += chg[i][j]
                stack.append((c-1, t+1, new_cur, new_s))

print(ans)