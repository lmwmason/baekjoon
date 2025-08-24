a = input()
b = input()
c = input()

arr = [[[0] * (len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            arr[i][j][k] = arr[i-1][j-1][k-1] + 1 if a[i-1] == b[j-1] and b[j-1] == c[k-1] else max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = -1
for i in range(len(a)+1):
    for j in range(len(b)+1):
        ans = max(max(arr[i][j]), ans)

print(ans)