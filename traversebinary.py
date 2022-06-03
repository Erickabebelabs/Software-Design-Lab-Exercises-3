#Pre-Oder Traversal/In-Order Traversal/Post-Order Traversal
class Node:
   def __init__(self, key):
      self.left = None
      self.right = None
      self.val = key

def printInorder(root):

   if root:
      printInorder(root.left)
      print(root.val),
      printInorder(root.right)

def printPostorder(root):

   if root:
      printPostorder(root.left)
      printPostorder(root.right)
      print(root.val),

def printPreorder(root):

   if root:
      print(root.val),
      printPreorder(root.left)
      printPreorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(" THE PRE-ORDER TRAVERSAL OF THE BINARY TREE IS:")
printPreorder(root)
print("\n THE IN-ORDER TRAVERSAL OF THE BINARY TREE IS:")
printInorder(root)
print("\n THE POST-ORDER TRAVERSAL OF THE BINARY TREE IS:")
printPostorder(root)