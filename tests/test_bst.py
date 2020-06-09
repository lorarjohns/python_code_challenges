from structures.bst import BST, Node

bst = BST()
bst.root = Node(10)
bst.root.left = Node(7)
bst.root.left.right = Node(9)
bst.root.right = Node(15)

print(bst)