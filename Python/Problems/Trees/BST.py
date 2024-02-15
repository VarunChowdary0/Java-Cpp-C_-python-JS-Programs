class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BSTTree:
    def __init__(self,root= None):
        self.root = root 
    def insert(self,x):
        if self.root == None:
            new_node = Node(x)
            self.root = new_node
        self.checkPosition(self.root,x)
    def checkPosition(self,current:Node,val):
        if current == None:
            new_node = Node(val)
            current = new_node
        elif val > current.data:
            current.right = self.checkPosition(current.right,val)
        elif val < current.data:
            current.left = self.checkPosition( current.left,val)
        return current
    
    def traverse(self):
        current = self.root
        self._traverse_inorder(current)
        print()
    def _traverse_inorder(self,current):
        if current :
            self._traverse_inorder(current.left)
            print(current.data,end=" ")
            self._traverse_inorder(current.right)

BST = BSTTree()
BST.insert(50)
BST.insert(100)
BST.insert(40)
BST.insert(20)
BST.insert(60)
BST.insert(10)
BST.insert(11)
BST.insert(14)
BST.traverse()
