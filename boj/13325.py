class Tree:
    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child



k = int(input())
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])


root = Tree(0)
node = root
while(len(arr)>0):
    num1 = arr.pop()
    num2 = arr.pop()
    node1 = Tree(num1)
    node2 = Tree(num2)
    node = Tree(node.data,node1,node2)

print(root.data)