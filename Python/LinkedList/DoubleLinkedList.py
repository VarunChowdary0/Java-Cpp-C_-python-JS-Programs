class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def insertEnd(self,value):
        self.length+=1
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def insertStart(self,value):
        self.length+=1
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    
    def insertAt(self,position,value):
        if position > self.length:
            print("Index out of Bound")
            return
        if position == self.length:
            self.insertEnd(value)
        else:
            new_node = Node(value)
            mid = self.length//2
            if position < mid:
                print("<")
                current = self.head
                for i in range(position-1):
                    current = current.next
                    print(i)
                new_node.next = current.next
                current.next.previous = new_node
                new_node.previous = current
                current.next = new_node                
            else:
                current = self.tail
                for i in range(self.length,position-1,-1):
                    current = current.previous
                new_node.next = current.next
                current.next.previous = new_node
                new_node.previous = current
                current.next = new_node 

    def deleteEnd(self):
        if self.head == None:
            print("List is Empty")
            return
        self.tail = self.tail.previous
        self.tail.next = None
        self.length-=1
    
    def deleteStart(self):
        if self.head == None:
            print("List is Empty")
            return
        self.head = self.head.next
        self.head.previous = None
        self.length-=1

    def traverse(self):
        if self.head == None:
            print("List is Empty")
            return
        current = self.head
        while current.next:
            print(current.data," <--> ",end=" ")
            current = current.next
        print("None")

DLL = DoubleLinkedList()
DLL.insertEnd(10)
DLL.insertEnd(20)
DLL.insertEnd(30)
DLL.insertEnd(40)
DLL.insertEnd(70)
DLL.insertStart(0)
DLL.traverse()
# DLL.deleteEnd()
# DLL.traverse()
# DLL.deleteStart()
# DLL.traverse()
DLL.insertAt(2,50)
DLL.traverse()
print("L: ",DLL.length)
DLL.insertAt(3,90)
DLL.traverse()