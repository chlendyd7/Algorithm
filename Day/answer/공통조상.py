# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&problemLevel=7&problemLevel=8&contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=8&pageSize=10&pageIndex=1

from collections import defaultdict, deque

def solution():
    V, E = node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))

    parent = [0] * (V+1)
    children = [[] for _ in range(V+1)]
    
    for i in range(0, E*2, 2):
        p = edges[i]
        c = edges[i+1]
        
        parent[c] = p
        children[p].append(c)
    ancestors = set()
    current = node1
    
    while current:
        ancestors.add(current)
        current = parent[current]


    current = node2
    while current not in ancestors:
        current = parent[current]
    lca = current

    count = 0
    stack = [lca]
    
    while stack:
        node = stack.pop()
        count += 1
    
        for child in children[node]:
            stack.append(child)
    
    return f'{lca} {count}'

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
