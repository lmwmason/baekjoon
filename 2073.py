
d, p = map(int, input().split())
l = [0] * 360
c = [0] * 360

for i in range(p):
    l[i], c[i] = map(int, input().split())

dt = [0] * 100010
dt[0] = 9000000
for i in range(p):
    for j in range(d, l[i] - 1, -1):
        dt[j] = max(dt[j], min(dt[j - l[i]], c[i]))

print(dt[d])
