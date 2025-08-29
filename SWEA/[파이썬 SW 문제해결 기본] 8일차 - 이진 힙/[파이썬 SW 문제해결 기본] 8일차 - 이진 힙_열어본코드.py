def min_heap(tree, val):
    while True:
        for i in range(1, len(tree)):
            tree[i] = val[0]
            val.pop(0)
            while i > 0 and tree[i] < tree[i//2]:
                tree[i], tree[i//2] = tree[i//2], tree[i]
                i //= 2
        if len(val) == 0:
            break

    return tree

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    val = list(map(int, input().split()))

    tree = [0] * (N+1)
    heap = min_heap(tree, val)

    parent = N // 2
    result = 0
    while parent:
        result += heap[parent]
        parent //= 2
    
    print(f'#{tc} {result}')
