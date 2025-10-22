from collections import defaultdict

def find_lca(node1, node2, parent):
    ancestor = set()
    while node1:
        ancestor.add(node1)
        node1 = parent.get(node1, None)
    while node2:
        if node2 in ancestor:
            return node2
        node2 = parent.get(node2, None)
    return None

def subtree_count(lca, graph):
    count = 1
    for node in graph[lca]:
        count += subtree_count(node, graph)

    return count
def solution():
    V, E, node1, node2 = map(int, input().split())
    lst = list(map(int ,input().split()))

    graph = defaultdict(list)
    parent = {}
    for i in range(0, E*2, 2):
        start, end = lst[i], lst[i+1]
        graph[start].append(end)
        parent[end] = start

    lca = find_lca(node1, node2, parent)
    cnt = subtree_count(lca, graph)

    return lca, cnt


T = int(input())
for t in range(1, T+1):
    lca, cnt = solution()
    print(f'#{t} {lca} {cnt}')
