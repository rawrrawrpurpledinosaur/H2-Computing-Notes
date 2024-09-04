class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree: 
    def __init__(self): 
        self.root = None

    def insert(self, data):
        if self.root == None: 
            self.root = Node(data)
        else: 
            probe = self.root
            if data < probe.data: 
                if probe.left == None: 
                    probe.left = Node(data)
                else: 
                    probe = probe.left
            else:
                if probe.right == None: 
                    probe.right = Node(data)
                else: 
                    probe = probe.right
    
    def search(self, target): 
        probe = self.root
        while probe != None: 
            if probe.data == target: 
                return True
            elif target < probe.data:
                probe = probe.left
            else:
                probe = probe.right 

        return False

    def inorder(self, node):
        # Left -> Root -> Right
        if node != None: 
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def preorder(self, node):
        # Root -> Left -> Right
        if node != None: 
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self, node):
        # Left -> Right -> Root
        if node != None: 
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def __str__(self):
        ret = ""
        for i in self.inorder(self.root):
            ret += str(i) + " "
        return ret

# test every function 
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.search(3))
bst.inorder(bst.root)
bst.preorder(bst.root)
bst.postorder(bst.root)
print(bst)

