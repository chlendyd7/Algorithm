# https://www.acmicpc.net/problem/5639

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if current.data > data:
                    if current.left == None:
                        current.left = Node(data)
                        break
                    current = current.left

                if current.data < data:
                    if current.right == None:
                        current.right = Node(data)
                        break
                    current = current.right

    def postOrder(self, node=None):
        global answer

        if node == None:
            node = self.root
        
        if node.left != None:
            self.postOrder(node.left)
        if node.right != None:
            self.postOrder(node.right)
        answer.append(node.data)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left is not None or node.right is not None:
                if node.left is not None:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right is not None:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:
        break
answer = []
tree.print_tree()
tree.postOrder()
tree.print_tree()
# print('\n'.join(map(str,answer)))

                    