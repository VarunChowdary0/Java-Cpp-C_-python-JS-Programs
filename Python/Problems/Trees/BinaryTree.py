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

def heigth(root:Node):
    if root == None:
        return 0
    else:
        lheigth = heigth(root.left)
        rheigth = heigth(root.right)

        if lheigth > rheigth:
            return lheigth+1
        else:
            return rheigth+1

def levelOrder(root:Node):
    h = heigth(root)
    for i in range(1,h+1):
        printLevel(root,i)

def printLevel(root:Node,level):
    if not root:
        return
    elif level == 1:
        print(root.data,end="  ")
    else:
        printLevel(root.left,level-1)
        printLevel(root.right,level-1)

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

print("\nHeigth: ",heigth(root))
print("Level Order: ",end=" ")
levelOrder(root)