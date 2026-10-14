def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, x, y):
    parent_x = find(parent, x)
    parent_y = find(parent, y)
    if parent_x > parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


def solution():
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append((w, n1, n2))
    
    graph.sort()
    total = 0
    parent = [i for i in range(V+1)]

    for w, s1, s2 in graph:
        if find(parent, s1) != find(parent, s2):
            union(parent, s1, s2)
            total += w
            
        
    return total

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
