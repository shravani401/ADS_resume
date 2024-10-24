class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self):  
        self.root = None
    
    def add(self, value):  
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_to_tree(self.root, value)
    
    def _add_to_tree(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_to_tree(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_to_tree(current_node.right, value)

    def in_order(self, node): 
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def pre_order(self, node): 
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node): 
        if node:
            self.post_order(node.left)  
            self.post_order(node.right)  
            print(node.value)


# Create the tree and insert nodes
t1 = TreeNode()
t1.add(20)
t1.add(10)
t1.add(11)
t1.add(4)
t1.add(3)

# Inorder traversal
print("Inorder Traversal:")
t1.in_order(t1.root)
print()

# Preorder traversal
print("Preorder Traversal:")
t1.pre_order(t1.root)
print()

# Postorder traversal
print("Postorder Traversal:")
t1.post_order(t1.root)
print()
