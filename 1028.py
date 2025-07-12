R, C = map(int, input().split())
place = [[0] * (C + 2) for _ in range(R + 2)]


for i in range(1, R + 1):
    s = input()
    for j in range(1, C + 1):
        place[i][j] = int(s[j - 1])


left_down = [[0] * (C + 2) for _ in range(R + 2)]
right_down = [[0] * (C + 2) for _ in range(R + 2)]
left_up = [[0] * (C + 2) for _ in range(R + 2)]
right_up = [[0] * (C + 2) for _ in range(R + 2)]


for i in range(R, 0, -1):
    for j in range(1, C + 1):
        if place[i][j]:
            left_down[i][j] = left_down[i+1][j-1] + 1
            right_down[i][j] = right_down[i+1][j+1] + 1


for i in range(1, R + 1):
    for j in range(1, C + 1):
        if place[i][j]:
            left_up[i][j] = left_up[i-1][j-1] + 1
            right_up[i][j] = right_up[i-1][j+1] + 1


ans = 0

for i in range(1, R + 1):
    for j in range(1, C + 1):
        start = ans if ans else 1
        for k in range(start, min(left_down[i][j], right_down[i][j]) + 1):
            target_row = i + (k - 1) * 2
            if target_row > R + 1: break
            if place[target_row][j] and left_up[target_row][j] >= k and right_up[target_row][j] >= k:
                ans = k
        for k in range(start, min(right_down[i][j], right_up[i][j]) + 1):
            target_col = j + (k - 1) * 2
            if target_col > C + 1: break
            if place[i][target_col] and left_up[i][target_col] >= k and left_down[i][target_col] >= k:
                ans = k


print(ans)