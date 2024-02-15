class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root:Node):
    if not root :
        return
    print(root.data,end="  ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root:Node):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def postOrder(root:Node):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

print("Preorder: ",end=" -> ")
preOrder(root)
print("\nInorder: ",end=" -> ")
inOrder(root)
print("\nPost Order: ",end=" -> ")
postOrder(root)
