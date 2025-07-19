def solve():
    n = int(input())
    sti = []
    for _ in range(2):
        row = list(map(int, input().split()))
        sti.append(row)

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = sti[0][0]
    dp[1][0] = sti[1][0]

    if n == 1:
        return max(dp[0][0], dp[1][0])

    dp[0][1] = dp[1][0] + sti[0][1]
    dp[1][1] = dp[0][0] + sti[1][1]

    for j in range(2, n):
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + sti[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + sti[1][j]

    return max(dp[0][n - 1], dp[1][n - 1])



t = int(input())
for _ in range(t):
    result = solve()
    print(result)