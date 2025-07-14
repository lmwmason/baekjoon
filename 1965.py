def lis(array):
    n = len(array)
    dp = [1] * n
    for i in range(1,n):
        for j in range(i):
            if array[j] < array[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    return max(dp)

_ = input()
arr = list(map(int, input().split()))
print(lis(arr))