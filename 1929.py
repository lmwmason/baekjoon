a,b = map(int, input().split())
arr = [0 for _ in range(b+2)]
arr[1] = 1

for i in range(2, b+1):
    for j in range(i, (b+1)//i+1):
        arr[i*j] = 1

for i in range(a,b+1) :
    if arr[i] == 0:
        print(i)