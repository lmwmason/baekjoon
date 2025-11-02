import sys
N, K = map(int, sys.stdin.readline().split())

arr = [i + 1 for i in range(N)]
result = []
idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)
    removed_person = arr.pop(idx)
    result.append(removed_person)
    
print(f"<{', '.join(map(str, result))}>")