'''
자료구조.최소 패닝트리.main의 Docstring
1. 크루스칼 알고리즘 (Kruskal's Algorithm)
가장 적은 비용의 간선부터 차례대로 선택하는 방식입니다. 
Union-Find(서로소 집합) 자료구조를 반드시 함께 사용해야 합니다.
'''

import sys

# 1. 부모 노드 찾기 (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 2. 두 노드 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 예시 처리
v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v + 1)]

edges = []
for _ in range(e):
    u, v_node, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, u, v_node))

# 비용 순으로 정렬
edges.sort()

total_cost = 0
for cost, u, v_node in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, u) != find_parent(parent, v_node):
        union_parent(parent, u, v_node)
        total_cost += cost

print(total_cost)