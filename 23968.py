import sys

n, k = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))
i = 0
k_cnt = 0
state_ = False
for i in range(n) :
    state = True
    for j in range(n-i-1) :
        if li[j] > li[j+1] :
            state = False
            li[j], li[j+1] = li[j+1], li[j]
            k_cnt += 1
            if k_cnt == k :
                print(li[j], li[j+1])
                state_ = True
    if state_ : break
    if state : break
if not state_: print(-1)