class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def traverse(self):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

CLL = CircularLinkedList()
CLL.insert(10)
CLL.insert(20)
CLL.insert(30)
CLL.insert(40)

CLL.traverse()
