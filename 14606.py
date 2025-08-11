n = int(input())
sum_ = 0
arr = list()
while True :
    for i in arr :
        n1 = i//2
        n2 = n - n1
        sum_+= n1 * n2
        n//=2
        if n1 == 1 and n2 == 1:
            break
