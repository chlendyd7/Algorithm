import sys
sys.setrecursionlimit(10**6)  # 재귀 한도를 늘립니다.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
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
                    if current.right = None:
                        current.right = Node(data)
                        break
                    current = current.right
    
    def postOrder(self ,node=None):
        global answer

tree = Tree()
while True:
    try:
        tree.add(int(input()))