import sys

input = sys.stdin.readline

fib = [1,1]
i = 1
while fib[-1] < 10**100:
    fib.append(fib[i]+fib[i-1])
    i+=1

def get_fib_num(a,b) :
    global fib
    num_before_a,num_before_b = 0,0
    for i in range(0,len(fib)):
        if fib[i] >= a and num_before_a == 0:
            num_before_a = i
        if fib[i] > b and num_before_b == 0:
            num_before_b = i
    return num_before_b-num_before_a

while True:
    a,b = map(int , input().split(" "))
    if a == 0 and b == 0:
        break
    print(get_fib_num(a,b))