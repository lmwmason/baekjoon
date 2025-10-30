"""BOJ 10828"""

Stack = list()

class StackFun :
    def __init__(self, Stack) :
        self.stack = Stack
    
    def push(self, x) :
        self.stack.append(x)
    def pop(self) :
        if(len(self.stack)==0) :
            return -1
        return self.stack.pop()
        
    def size(self) :
        return len(self.stack)
    def empty(self) :
        if(len(self.stack)==0) :
            return 1
        return 0
    def top(self) :
        if(len(self.stack)==0) :
            return -1
        return self.stack[-1]
    
stackfun = StackFun(Stack)


for i in range(int(input())) :
    CMD = input()
    if(CMD[0:4]=="push") :
        CMDM, Num = CMD.split()
        stackfun.push(Num)
    elif(CMD=="pop") :
        print(stackfun.pop())
    elif(CMD=="size") :
        print(stackfun.size())
    elif(CMD=="empty") :
        print(stackfun.empty())
    else :
        print(stackfun.top())
