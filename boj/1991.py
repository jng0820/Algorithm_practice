
class Node():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree():
    def __init__(self, node):
        self.root = node

    def insert(self, node1, node2, node3):
        node1.left = node2
        node2.right = node3

    def preorder(self,node):
        print(chr(node.data), end='')
        if(node.left != None):
            self.preorder(self,node.left)
        if (node.right != None):
            self.preorder(self,node.right)

    def inorder(self,node):
        if(node.left != None):
            self.inorder(self,node.left)

        print(chr(node.data), end='')
        if (node.right != None):
            self.inorder(self,node.right)

    def postorder(self,node):
        if(node.left != None):
            self.postorder(self,node.left)
        if (node.right != None):
            self.postorder(self,node.right)
        print(chr(node.data), end='')


value = input()
value = int(value)

node = []
for i in range(value):
    node.append(Node(data = 65+i))

tree = BTree(node[0])
for i in range(value):
    str = []
    str = input().split()
    if(str[1] != '.'):
        node[ord(str[0]) - 65].left = node[ord(str[1]) - 65]
    if (str[2] != '.'):
        node[ord(str[0]) - 65].right = node[ord(str[2]) - 65]

BTree.preorder(BTree, node=tree.root)
print()
BTree.inorder(BTree,node=tree.root)
print()
BTree.postorder(BTree,node=tree.root)
