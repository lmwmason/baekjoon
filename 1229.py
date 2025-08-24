import sys
input=sys.stdin.readline

n=int(input())
h=[]
i,j=1,1
while i*j<=n:
    h.append(i*j)
    i+=1
    j+=2

dp=[0]
for x in range(1,n+1):
    m=99999999999999999999999999999999999999999999
    for v in h:
        if v>x: break
        m=min(m,1+dp[x-v])
    dp.append(m)

print(dp[-1])