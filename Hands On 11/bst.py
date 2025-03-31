class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.value:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        
        return root

    def search_node(self, root, key):
        if root is None or root.value == key:
            return root
        
        if key < root.value:
            return self.search_node(root.left, key)
        
        return self.search_node(root.right, key)

    def delete_node(self, root, key):
        if root is None:
            return root
        
        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
        
            temp = self.find_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)
        
        return root

    def find_min_value_node(self, root):
        current = root
        
        while current.left is not None:
            current = current.left
        
        return current

    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []


bst = BinarySearchTree()
bst_root = None
bst_root = bst.insert_node(bst_root, 50)
bst_root = bst.insert_node(bst_root, 30)
bst_root = bst.insert_node(bst_root, 70)
bst_root = bst.insert_node(bst_root, 40)
bst_root = bst.insert_node(bst_root, 10)
bst_root = bst.insert_node(bst_root, 60)
bst_root = bst.insert_node(bst_root, 20)

print("Inorder Traversal of BST:", bst.inorder(bst_root))
print("Minimum Value Node: ", bst.find_min_value_node(bst_root).value)

bst_root = bst.delete_node(bst_root, 10)
print("Inorder Traversal of the Tree after deletion of Node 10:", bst.inorder(bst_root))

bst_root = bst.delete_node(bst_root, 50)
print("Inorder Traversal of the Tree after deletion of Node 50:", bst.inorder(bst_root))

bst_root = bst.delete_node(bst_root, 20)
print("Inorder Traversal of the Tree after deletion of Node 20:", bst.inorder(bst_root))
print("Minimum Value Node after deletion of Node 10, 20, 50: ", bst.find_min_value_node(bst_root).value)

bst_root = bst.delete_node(bst_root, 100)
print("Inorder Traversal after deletion of non-existing node:", bst.inorder(bst_root))