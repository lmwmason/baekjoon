_ = int(input())
state = 0

dp = [0 for _ in range(1000001)]
for i in range(1, 447):
    n = i*(i+1)//2
    for j in range(i + 1):
        dp[n+j] = i

a = list(map(int, input().split()))

for i in a:
    state ^= dp[i]

if state == 0:
    print("cubelover")
else :
    print("koosaga")
    