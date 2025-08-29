def min_heap(tree, val):
    min_val = min(val)
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