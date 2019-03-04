import sys
sys.setrecursionlimit(10**6)

pre_answer = []
post_answer = []
class Node:
    index =0
    x_val = 0
    y_val = 0
    left = 0
    right = 0
    def __init__(self,index, x_val, y_val):
        self.index = index
        self.x_val = x_val
        self.y_val = y_val
    
def preorder(root):
    global pre_answer

    pre_answer.append(root.index)
    if(root.left == 0 and root.right == 0):
        return
    if(root.left != 0):
        preorder(root.left)
    if(root.right != 0):
        preorder(root.right)
    
def postorder(root):
    global post_answer

    if(root.left != 0):
        postorder(root.left)
    if(root.right != 0):
        postorder(root.right)
    post_answer.append(root.index)
    if(root.left == 0 and root.right == 0):
        return
def solution(nodeinfo):
    global pre_answer
    global post_answer
    answer = []
    node = [[i+1, val[0], val[1]] for i, val in enumerate(nodeinfo)]
    node.sort(key=lambda x: x[1], reverse = False)
    node.sort(key=lambda x : x[2], reverse=True)
    root = Node(node[0][0],node[0][1],node[0][2])
    del node[0]
    while(len(node)):
        pointer = root
        while(True):
            if(node[0][1] < pointer.x_val):
                if(pointer.left == 0):
                    pointer.left = Node(node[0][0],node[0][1],node[0][2])
                    del node[0]
                    break
                pointer = pointer.left
            else:
                if(pointer.right == 0):
                    pointer.right = Node(node[0][0],node[0][1],node[0][2])
                    del node[0]
                    break
                pointer = pointer.right
    preorder(root)
    postorder(root)
    answer.append(pre_answer)
    answer.append(post_answer)
    return answer