def lis(a,num) :
    lis_dp = [1 for _ in range(num)]
    for i in range(num):
        for j in range(i):
            if a[j] < a[i] and lis_dp[i] < lis_dp[j] + 1:
                lis_dp[i] = lis_dp[j] + 1
    return max(lis_dp)

def lds(a,num) :
    lds_dp = [1 for _ in range(num)]
    for i in range(num):
        for j in range(i):
            if a[j] > a[i] and lds_dp[i] < lds_dp[j] + 1:
                lds_dp[i] = lds_dp[j] + 1
    return max(lds_dp)

n = int(input())
arr = list(map(int, input().split()))
lbs = list()
for i in range(n) :
    lbs.append(lis(arr[:i+1], i+1)+lds(arr[(i):], n-i)-1)
print(max(lbs))