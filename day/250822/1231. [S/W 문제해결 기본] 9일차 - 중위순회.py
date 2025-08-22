def solution():
    N = int(input())
    tree = [(0,0)] * (N+1)
    chars = [''] * (N+1)
    for _ in range(N):
        node, word, *childs = input().split()
        node = int(node)
        chars[node] = word
        left, right = 0, 0
        if len(childs) >= 1:
            left = int(childs[0])
        if len(childs) >= 2:
            right = int(childs[1])
        tree[node] = (left, right)

    result = []
    def inorder(node):
        left, right = tree[node]
        if left:
            inorder(left)
        result.append(chars[node])
        if right:
            inorder(right)
    
    inorder(1)
    return ''.join(result)

for t in range(1, 11):
    print(f'#{t} {solution()}')