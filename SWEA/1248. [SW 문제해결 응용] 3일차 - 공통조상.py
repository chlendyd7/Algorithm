# LCA, Lowest Common Ancestor
from collections import defaultdict

def find_lca(node1, node2, parent):
    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = parent.get(node1, None)
    while node2:
        if node2 in ancestors:
            return node2
        node2 = parent.get(node2, None)
    return None

def subtree_size(root, graph):
    count = 1
    for child in graph[root]:
        count += subtree_size(child, graph)
    return count

def solution():
    V, E, node1, node2 = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = defaultdict(list)
    parent = {}

    for i in range(0, E*2, 2):
        start, end = lst[i], lst[i+1]
        graph[start].append(end)
        parent[end] = start
    print(graph)
    print(parent)
    lca = find_lca(node1, node2, parent)
    size = subtree_size(lca, graph)
    return lca, size

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')