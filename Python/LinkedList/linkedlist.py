class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def insertEnd(self,x):
        new_node = Node(x)
        self.length+=1
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insertStart(self,x):
        new_node = Node(x)
        self.length+=1
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def traverse(self):
        current = self.head
        while current:
            print(current.data," -> ",end=" ")
            current = current.next
        print("None")

    def deleteEnd(self):
        self.length-=1
        if self.head == None:
            print("List is Empty")
            return
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def deleteStart(self):
        self.length-=1
        if self.head == None:
            print("List is Empty")
            return
        else:
            self.head = self.head.next
            
    def getvalueAt(self,idx):
        if self.head == None:
            print("List is Empty")
            return
        if idx > self.length:
            print("Index out of Bound")
        else:
            current = self.head
            for i in range(idx):
                current = current.next
            return current.data
    
    def peek(self):
        return self.getvalueAt(self.length-1)
    
    def insertAt(self,position,value):
        if position > self.length:
            print("Index out of bound")
        else:
            self.length+=1
            new_node = Node(value)
            current = self.head
            for i in range(position-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def removeAt(self,index):
        if self.head == None:
            print("List is Empty")
            return
        if index > self.length-1:
            print("Index out of Bound")
            return
        current = self.head
        self.length-=1
        for i in range(index-1):
            current = current.next
        current.next = current.next.next

    def update(self,index,value):
        if self.head == None:
            print("List is empty")
            return
        if index > self.length:
            print("Index out of Bound")
            return
        current = self.head
        for i in range(index):
            current = current.next
        current.data = value
    def filterValue(self,value):
        if self.head == None:
            print("List is Empty")
            return
        current_position = 0
        current = self.head
        value_is_at = []
        while current.next:
            current_position+=1
            if current.data == value:
                value_is_at.append(current_position)
            current = current.next
        for i in range(len(value_is_at)):
            self.removeAt(value_is_at[i]-i-1)
LL = LinkedList()
LL.insertEnd(10)
LL.insertEnd(70)
LL.insertEnd(20)
LL.insertEnd(30)
LL.insertEnd(70)
LL.insertEnd(40)
LL.insertEnd(70)
LL.insertStart(0)
LL.insertStart(-10)
LL.traverse()
print(LL.getvalueAt(4))
print("Length: ",LL.length)
print("peek: ",LL.peek())
LL.insertAt(3,90)
LL.traverse()
print("Length: ",LL.length)
LL.removeAt(2)
LL.traverse()
print("Length: ",LL.length)
LL.update(2,100)
LL.traverse()
LL.insertAt(3,70)
LL.insertAt(5,70)
LL.traverse()
print("Length: ",LL.length)
LL.filterValue(70)
LL.traverse()
print("Length: ",LL.length)
