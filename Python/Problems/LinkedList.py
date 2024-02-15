class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertBeg(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    def insertEnd(self,x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def traverse(self):
        current = self.head
        if not current :
            print("List is Empty")
        else:
            while current:
                print(current.data,end=" -> ")
                current = current.next
            print("None")
    def length(self):
        current = self.head
        len = 0
        if not current :
            return len
        else:
            while current:
                len+=1
                current = current.next
            return len
    
    def getValueAt(self,idx):
        idx = idx+1
        if(idx>self.length()):
            return "Index out of Bound"
        else:
            current = self.head
            res = 0
            for i in range(idx):
                res = current.data
                current=current.next
        return res
    
    def updateValue(self,idx,val):
        if(idx>self.length()):
            print("Index out of Bound")
        else:
            current = self.head
            for i in range(idx):
                current=current.next
        current.data = val
    def getMiddle(self):
        l = self.length()
        mid = l//2
        return self.getValueAt(mid)
    def insertAt(self,idx,val):
        new_node = Node(val)
        if(idx>self.length()):
            print("Index out of Bound")
        else:
            current = self.head
            for i in range(idx-1):
                current=current.next
            new_node.next = current.next
            current.next = new_node
    def deleteEnd(self):
        if not self.head:
            return
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
    def deleteStart(self):
        if not self.head:
            return
        else:
            temp = self.head
            self.head = temp.next
            temp = None
    def remove(self,idx):
        if(idx>self.length()):
            print("Index out of Bound")
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            print("Removed: ",current.next.data)
            temp = current.next.next
            current.next = temp
    def makeCylic(self,idx):
        if(idx>self.length()):
            print("Index out of Bound")
        else:
            Pos = None
            count = 0
            current = self.head
            while current.next:
                current = current.next
                if count == idx-1:
                    Pos = current
                count+=1
            current.next = Pos 
    
    def isCyclic(self):
        if not self.head:
            return False
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = None
            
LL = LinkedList()
LL.insertEnd(10)
LL.insertEnd(20)
LL.insertEnd(30)
LL.insertEnd(40)
LL.insertEnd(50)
LL.insertBeg(0)
LL.updateValue(0,100)
LL.insertAt(2,1001)
LL.traverse()
print(LL.length())
print(LL.getValueAt(5))
print(LL.getMiddle())
LL.deleteEnd()
LL.deleteStart()
LL.remove(3)
LL.traverse()
LL.makeCylic(2)
LL.traverse()