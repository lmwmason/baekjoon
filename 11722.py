def lds(n, arr) :
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

n = int(input())
arr = list(map(int, input().split()))
print(lds(n, arr))