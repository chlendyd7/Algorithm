def preorder(node, tree, chars, result):
    if node == 0:
        return
    left, right = tree[node]
    result.append(chars[node])   # 현재
    preorder(left, tree, chars, result)   # 왼쪽
    preorder(right, tree, chars, result)  # 오른쪽

def inorder(node, tree, chars, result):
    if node == 0:
        return
    left, right = tree[node]
    inorder(left, tree, chars, result)    # 왼쪽
    result.append(chars[node])            # 현재
    inorder(right, tree, chars, result)   # 오른쪽

def postorder(node, tree, chars, result):
    if node == 0:
        return
    left, right = tree[node]
    postorder(left, tree, chars, result)  # 왼쪽
    postorder(right, tree, chars, result) # 오른쪽
    result.append(chars[node])            # 현재
