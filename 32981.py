def get_how_many_real_even_num(num) :
    if num==1 :
        return 5
    return 4*(pow(5, num-1, 1000000007))%1000000007

n = int(input())
for _ in range(n) :
    print(get_how_many_real_even_num(int(input())) % 1000000007)