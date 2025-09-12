def diff(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt

s = " " + input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

dp = [1000] * len(s)
dp[0] = 0

for i in range(1, len(s)):
    if dp[i-1] == 1000:
        continue
    for w in words:
        l = len(w)
        if i + l <= len(s) and sorted(s[i:i+l]) == sorted(w):
            dp[i+l-1] = min(dp[i+l-1], dp[i-1] + diff(s[i:i+l], w))

if dp[-1] != 1000:
    print(dp[-1])
    exit()
print(-1)
