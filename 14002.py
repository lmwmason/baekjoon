n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]
pre = [-1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            pre[i] = j

max_length = max(dp)
last_index = dp.index(max_length)

lis = []
index = last_index
while True :
    lis.append(arr[index])
    index = pre[index]
    if index == -1 :
        break;

lis.reverse()

print(max_length)
for i in lis :
    print(i, end=" ")