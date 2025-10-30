"""BOJ 9012"""

def IfTrue(InString) :
    OpenCnt = 0
    
    for i in InString :
        if i=="(" :
            OpenCnt+=1
        else :
            OpenCnt-=1
        if OpenCnt<0 :
            return False
    if OpenCnt==0 :
        return True
    return False

n = int(input())
for i in range(n) :
    print(["NO", "YES"][int(IfTrue(input()))])
