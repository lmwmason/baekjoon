n=int(input())
h=[]
i,j=1,1
while i*j<=n:
    h.append(i*j)
    i+=1
    j+=2

dp=[0]
for i in range(1,n+1):
    m=99999999999999999999999999999999999999999999
    for j in h:
        if j>i: break
        m=min(m,1+dp[i-j])
    dp.append(m)

print(dp[-1])