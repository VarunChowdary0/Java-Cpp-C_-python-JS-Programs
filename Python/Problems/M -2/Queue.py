current = 0
def CreateQueue():
    q = []
    return q
def isEmpty():
    if current == 0:
        return True
    return False
def isFull():
    if current == N:
        return True
    return False
def pop(queue):
    global current
    if(not isEmpty()):
        current-=1
        return queue.pop(0)
    else:
        return "Queue is Empty"
def push(queue,val):
    global current
    if not isFull():
        queue.append(val)
        current+=1
        return True
    return False
def peek(queue):
    if not isEmpty():
        return queue[0]
    return False

N = int(input("Enter Size: "))
q = CreateQueue()
print(isEmpty())
print(push(q,100))
print(push(q,200))
print(q)
print(pop(q))
print(pop(q))
print(pop(q))
print(q)