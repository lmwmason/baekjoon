n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
s = 0

for i in range(n):
    for j in range(n):
        if a[i] > b[j] != 0:
            s += 2
            a[i] = b[j] = 0
            break

for i in range(n):
    if not a[i]:
        continue
    for j in range(n):
        if a[i] == b[j] != 0:
            s += 1
            b[j] = 0
            break

print(s)
