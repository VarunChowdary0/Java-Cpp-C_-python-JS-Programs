class Stack:
    def __init__(self,q:list):
        self.q=q
        self.len = len(q)
    def push(self,x):
        self.q.append(x)
        self.len+=1
    def isEmpty(self):
        if self.len == 0:
            return True
        return False
    def pop(self):
        if not self.isEmpty():
            self.q.pop()
            self.len-=1
        else:
            print("Stack is empty")
    def top(self):
        print(self.q[self.len-1])
    def see(self):
        print(self.q)

stack = Stack([1,2,3])
stack.see()
stack.pop()
stack.see()
stack.top()
stack.push(4)
stack.see()