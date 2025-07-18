def solution(n) :
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n<=10 :
        return arr[n]
    else :
        for j in range(11,n+1) :
            arr.append(arr[j-1]+arr[j-5])
        return arr[-1]


n = int(input())
for i in range(n) :
    print(solution(int(input())))