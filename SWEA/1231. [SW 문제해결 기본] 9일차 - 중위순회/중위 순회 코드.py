def solution():
    N = int(input())
    chars = [''] * (N+1)
    tree = [(0,0)] * (N+1)   # (왼쪽, 오른쪽)

    for _ in range(N):
        data = input().split()
        node = int(data[0])
        chars[node] = data[1]
        left, right = 0, 0
        if len(data) >= 3:
            left = int(data[2])
        if len(data) >= 4:
            right = int(data[3])
        tree[node] = (left, right)
    print(tree)
    result = []

    def inorder(node):
        if node == 0:
            return
        left, right = tree[node]
        inorder(left)               # 왼쪽
        result.append(chars[node])  # 현재
        inorder(right)              # 오른쪽

    inorder(1)  # 루트는 항상 1번
    return "".join(result)


for t in range(1, 11):  # 총 10개의 테스트 케이스
    print(f'#{t} {solution()}')
