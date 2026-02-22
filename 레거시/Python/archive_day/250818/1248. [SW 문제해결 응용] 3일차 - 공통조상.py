# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD
# LCA, Lowest Common Ancestor

from collections import defaultdict

def find_lca(graph, node1, node2):
    check = set()
    while node1:
        node1 = graph.get(node1, None)
        check.add(node1)
    while node2:
        if node2 in check:
            return node2
        node2 = graph.get(node2, None)
    return None

def subtree_size(root, graph):
    count = 1
    for child in graph[root]:
        count += subtree_size(child, graph)
    return count

def solution():
    V, E, node1, node2 = map(int, input().split())
    lines = list(map(int, input().split()))

    graph = defaultdict(list)
    parents = {}
    for i in range(0, E*2, 2):
        start, end = lines[i], lines[i+1]
        graph[start].append(end)
        parents[end] = start
    lca = find_lca(parents, node1, node2) 
    size = subtree_size(lca, graph)
    return lca, size

T = int(input())
for t in range(1, T+1):
    lca, size = solution()
    print(f'#{t} {lca} {size}')
