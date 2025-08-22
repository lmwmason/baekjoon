n, p, q = map(int,input().split())
dic_ = {}
dic_[0] = 1

def ans(i):
    if i not in dic_:
        dic_[i] = ans(i//p) + ans(i//q)
    return dic_[i]

print(ans(n))