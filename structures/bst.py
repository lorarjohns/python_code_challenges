class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def _insert(self, val, root):
        node = Node(val)
        if root is None:
            root = node
        if root.val > val:
            if root.left is None:
                root.left = node
            else:
                self._insert(val, root.left)
        elif root.val < val:
            if root.right is None:
                root.right = node
            else:
                self._insert(val, root.right)

    def _search(self, val, root):
        if root is None or root.val == val:
            return root
        if root.val < val:
            return self._search(val, root.right)
        return self._search(val, root.left)

    def __repr__(self):
        return f"Node: {self.val}"

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if not self.left and not self.right:
    #         raise StopIteration
    #     return self.left, self.right



class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, root=None):
        if self.root is None:
            self.root = Node(val)
        
        root = self.root
        root._insert(val, root)

    def search(self, val, root=None):
        root = self.root
        if root is None:
            raise ValueError("No root in tree")
        return root._search(val, root)


if __name__ == "__main__":

    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(8)
    bst.insert(700)
    bst.insert(2)
    bst.insert(-22)
    def inorder(root): 
        if root: 
            inorder(root.left) 
            print(root) 
            inorder(root.right) 

    inorder(bst.root)
    