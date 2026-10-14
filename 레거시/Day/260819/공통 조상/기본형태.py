# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD
from collections import deque


def solution():
    V, E, S1, S2 = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    parent = [0] * (V+1)
    for i in range(0, E*2, 2):
        s, e = data[i], data[i+1]
        graph[s].append(e)
        parent[e] = s
    
    current = S1
    ancestor = set()
    while current:
        ancestor.add(current)
        current = parent[current]
    
    lca = 0
    current = S2
    while current:
        if current in ancestor:
            lca = current
            break
        current = parent[current]
    
    cnt = 0
    q = deque([lca])
    while q:
        cnt += 1
        now = q.popleft()
        for node in graph[now]:
            q.append(node)

    return f'{lca} {cnt}'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
