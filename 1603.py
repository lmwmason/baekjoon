import itertools

dp = {}

def sol(n):
    if n in dp:
        return dp[n]
    if n <= 1:
        dp[n] = 0
        return 0
    s = {sol(i) ^ sol(n - i - 2) for i in range(n - 1)}
    s |= {sol(i) ^ sol(n - i - 1) ^ 1 for i in range(n)}
    x = 0
    while x in s:
        x += 1
    dp[n] = x
    return x

for _ in range(3):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    pairs, singles = [], 0
    i = 0
    while i + 1 < n:
        r1, r2 = board[i], board[i + 1]
        j = 0
        while j < m:
            for k, grp in itertools.groupby(zip(r1[j:], r2[j:])):
                length = len(list(grp))
                if k == ('.', '.'):
                    pairs.append(length)
                elif '.' in k:
                    singles += length
                j += length
        i += 2
    if n % 2:
        singles += board[-1].count('.')
    result = singles % 2
    for p in pairs:
        result ^= sol(p)
    print('Y' if result else 'M')
