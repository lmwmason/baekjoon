from sys import stdin, stdout

DP = [[-1] * 51 for _ in range(51)]

def P(i):
    return 1 << i

def F(n, h):
    if n == 0:
        return 1 if h == 0 else 0
    if h < 0 or h > 50:
        return 0
    ret = DP[n][h]
    if ret != -1:
        return ret
    ret = F(n - 1, h + 1)
    if h > 0:
        ret += F(n - 1, h - 1)
    DP[n][h] = ret
    return ret

def Sol(n, h, f, k):
    if n == 0:
        return
    cnt = P(n - 1) - (0 if f else F(n - 1, h + 1))
    if k < cnt:
        stdout.write('(')
        Sol(n - 1, h + 1, f, k)
    else:
        stdout.write(')')
        Sol(n - 1, h - 1, f | (0 if h > 0 else 1), k - cnt)

def main():
    n, k = map(int, stdin.readline().split())
    if k >= P(n) - F(n, 0):
        stdout.write('-1\n')
    else:
        Sol(n, 0, 0, k)

if __name__ == "__main__":
    main()
