fib = [0,1]
for i in range(2,int(input())+1):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[-1])