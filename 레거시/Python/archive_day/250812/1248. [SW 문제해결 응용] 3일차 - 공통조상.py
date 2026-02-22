# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD
from collections import defaultdict

def lca(node1, node2, parent:dict):
    parents = set()
    while node1:
        parents.add(node1)
        node1 = parent.get(node1, None)

    while node2:
        if node2 in parents:
            return node2
        node2 = parent.get(node2, None)

    return None

def count_subtree(node, graph):
    count = 1
    for n in graph[node]:
        count += count_subtree(n, graph)
    return count

def solution():
    V,E, node1, node2 = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = defaultdict(list)
    parent = {}
    for i in range(0, E*2, 2):
        p, c = lst[i], lst[i+1]
        graph[p].append(c)
        parent[c] = p

    lc = lca(node1, node2, parent)
    cnt = count_subtree(lc, graph)

    return lc, cnt


T = int(input())
for t in range(1, T+1):
    parent, cnt = solution()
    print(f'#{t} {parent} {cnt}')
