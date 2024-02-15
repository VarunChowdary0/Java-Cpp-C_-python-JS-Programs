class MyQueue:
    def __init__(self, stack):
        self.stack = stack
        self.len = len(stack)

    def push(self, x):
        self.stack.append(x)
        self.len += 1
        print("PUSHED")

    def isEmpty(self):
        return self.len == 0

    def pop(self):
        if not self.isEmpty():
            x = self.stack.pop(0)
            self.len -= 1
            print("POPED", x)
        else:
            print("Stack is Empty")

    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.len - 1])

    def see(self):
        print(self.stack)

Q = MyQueue([1, 2, 3])
Q.see()
Q.pop()
Q.push(4)
Q.see()
Q.peek()
