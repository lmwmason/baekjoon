num = int(input())
in_ = list(input())

for _ in range(num-1):
    inin = input()
    for n in range(len(in_)):
        if in_[n] == inin[n]:
            continue
        else:
            in_[n] = "?"
print(*in_, sep = "")