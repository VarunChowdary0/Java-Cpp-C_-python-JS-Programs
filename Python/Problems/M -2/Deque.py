class DoubleQueue:
    def __init__(self, stack):
        self.stack = stack
        self.len = len(stack)

    def pushEnd(self, x):
        self.stack.append(x)
        self.len += 1
        print("pushEnd")

    def pushStart(self, x):
        self.stack.insert(x,0)
        self.len += 1
        print("pushstart")

    def isEmpty(self):
        return self.len == 0

    def popStart(self):
        if not self.isEmpty():
            x = self.stack.pop(0)
            self.len -= 1
            print("POPED", x)
        else:
            print("Stack is Empty")

    def popEnd(self):
        if not self.isEmpty():
            x = self.stack.pop()
            self.len -= 1
            print("POPED", x)
        else:
            print("Stack is Empty")

    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.len - 1])

    def see(self):
        print(self.stack)

Q = DoubleQueue([1, 2, 3])
Q.see()
Q.popStart()
Q.pushEnd(4)
Q.see()
Q.popEnd()
Q.pushStart(0)
Q.peek()
Q.see()