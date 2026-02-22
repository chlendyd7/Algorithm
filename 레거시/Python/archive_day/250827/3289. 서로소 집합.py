def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    ans = []
    
    for _ in range(m):
        op, a, b = map(int input().split())
        if op == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print('1', end='')
            else:
                print('0', end='')
