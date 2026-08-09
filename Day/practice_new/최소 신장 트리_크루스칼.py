#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS26fKIucDFAVT&categoryId=AWUS26fKIucDFAVT&categoryType=CODE&problemTitle=%EC%B5%9C%EC%86%8C+%EC%8B%A0%EC%9E%A5+%ED%8A%B8%EB%A6%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(V):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    
    edges.sort()
    parent = [i for i in range(V+1)]
    
    total_weight = 0
    cnt = 0
    
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_weight += w
            cnt += 1
            if cnt == V:
                break
    
def solve_kruskal():
    T = int(input())
    for t in 

