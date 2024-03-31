class twoStacks:
    def __init__(self,n):
        self.size= n
        self.arr=[None]*n
        self.top1= -1
        self.top2 = self.size
    def push1(self,x):
        if self.top1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x
            print("pushed:" ,x)
        else:
            print("stack 1 overflow")
    def push2(self,x):
        if self.top1 < self.top2:
            self.top1 -= 1
            self.arr[self.top1] = x
            print("pushed:" ,x)
        else:
            print("stack 2 overflow")
    def pop1(self):
        if self.top1 >=0:
            x= self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("stack1 underflow")
    def pop2(self):
        if self.top2 < self.size:
            x= self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("stack2 underflow")

#example usage:
stacks = twoStacks(5)
stacks.push1(1)
stacks.push2(2)
stacks.push2(11)
stacks.push2(12)
stacks.push1(4)
stacks.push2(8)
stacks.push1(6)
print("popped", stacks.pop1())
print("popped", stacks.pop2())
print("popped", stacks.pop2())
print("popped", stacks.pop2())
print("popped", stacks.pop1())
print("popped", stacks.pop2())
print("popped", stacks.pop1())
