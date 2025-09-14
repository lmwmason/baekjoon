import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
ans = 0

if n == 1:
    a.sort()
    ans = sum(a[:5])
else:
    m = [min(a[0], a[5]), min(a[1], a[4]), min(a[2], a[3])]
    m.sort()
    m1, m2, m3 = m[0], m[0]+m[1], sum(m)

    c1 = 4*(n-2)*(n-1) + (n-2)**2
    c2 = 4*(n-1) + 4*(n-2)
    c3 = 4

    ans = m1*c1 + m2*c2 + m3*c3

print(ans)
