def find_parents(parent, x):
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
total_love = 0
maintained_love = 0

graph = []

for _ in range(m):
    u, v, c, d = map(int, input().split())
    
    total_love += c
    if d == 1:
        if find_parents(parent, u) != find_parents(parent, v):
            union_parent(parent, u, v)
        maintained_love += c
    else:
        edges.append((c, u, v))

edges.sort(key=lambda x: x[0], reverse=True)

for cost, u in edges:
    if find_parents(parent, u) != find_parents(parent, v):
        union_parent(parent, u, v)
        maintained_love += cost

print(total_love - maintained_love)

