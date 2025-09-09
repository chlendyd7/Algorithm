def union(x, y):
    parent_a, parent_b = find(x), find(y)
    if parent_b > parent_a:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]



T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    result = []
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union(a, b)
        else:
            result.append('1' if find(a) == find(b) else '0')

    r = ''.join(map(str, result))
    print(f'#{t} {r}')