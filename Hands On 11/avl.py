class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if not root:
            return Node(key)

        if key < root.value:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_tree_height(root.left), self.get_tree_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_tree_height(z.left), self.get_tree_height(z.right))
        y.height = 1 + max(self.get_tree_height(y.left), self.get_tree_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_tree_height(z.left), self.get_tree_height(z.right))
        y.height = 1 + max(self.get_tree_height(y.left), self.get_tree_height(y.right))

        return y

    def get_tree_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_tree_height(root.left) - self.get_tree_height(root.right)

    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

    def search_node(self, root, key):
        if not root or root.value == key:
            return root

        if key < root.value:
            return self.search_node(root.left, key)

        return self.search_node(root.right, key)

    def delete_node(self, root, key):
        if not root:
            return root

        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.find_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        root.height = 1 + max(self.get_tree_height(root.left), self.get_tree_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def find_min_value_node(self, root):
        current = root

        while current.left:
            current = current.left

        return current


avl = AVLTree()
avl_root = None

avl_root = avl.insert_node(avl_root, 50)
avl_root = avl.insert_node(avl_root, 30)
avl_root = avl.insert_node(avl_root, 40)
avl_root = avl.insert_node(avl_root, 70)
avl_root = avl.insert_node(avl_root, 10)
avl_root = avl.insert_node(avl_root, 60)
avl_root = avl.insert_node(avl_root, 20)

print("Inorder Traversal of AVL Tree:", avl.inorder(avl_root))
print("Minimum Value Node: ", avl.find_min_value_node(avl_root).value)

avl_root = avl.delete_node(avl_root, 10)
print("Inorder Traversal after deletion of 10:", avl.inorder(avl_root))

avl_root = avl.delete_node(avl_root, 50)
print("Inorder Traversal after deletion of 50:", avl.inorder(avl_root))

avl_root = avl.delete_node(avl_root, 20)
print("Inorder Traversal after deletion of 20:", avl.inorder(avl_root))
print("Minimum Value Node after deletion of Node 10, 20, 50: ", avl.find_min_value_node(avl_root).value)

avl_root = avl.delete_node(avl_root, 100)
print("Inorder Traversal after deletion of non-existing node:", avl.inorder(avl_root))