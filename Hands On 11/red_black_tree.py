class Node:
    def __init__(self, data):
        self.data = data
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "black"
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
    
        if y.left != self.TNULL:
            y.left.parent = x
    
        y.parent = x.parent
    
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
    
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
    
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
    
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
    
        y.right = x
        x.parent = y

    def insert_node(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
    
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
    
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            return

        if node.parent.parent is None:
            return

        self.fix_insert_node(node)

    def fix_insert_node(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
    
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
    
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
    
            if k == self.root:
                break
    
        self.root.color = "black"

    def print_tree(self):
        self.print_helper(self.root, "", True)

    def print_helper(self, node, indent, last):
        if node != self.TNULL:
            print(indent, end="")
    
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
    
            s_color = node.color
            print(f"{node.data}({s_color})")
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)


rbt = RedBlackTree()

rbt.insert_node(50)
rbt.insert_node(30)
rbt.insert_node(40)
rbt.insert_node(70)
rbt.insert_node(10)
rbt.insert_node(60)
rbt.insert_node(20)

print("Inorder Traversal of Red-black Tree:", rbt.print_tree())