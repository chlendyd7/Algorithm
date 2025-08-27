'''
2️⃣ 프림(Prim) 알고리즘
정점 중심 접근
단계:
    임의 정점 선택 → MST 집합에 추가
    MST 집합에서 연결된 가장 작은 간선 선택
    새로운 정점을 MST에 추가
    모든 정점이 MST에 포함될 때까지 반복

🔹 필요 자료 구조
우선순위 큐(Priority Queue, heapq): 최소 간선 선택

🔹 프림 특징

정점 중심 → 정점 수 적을 때 유리
구현: heap 사용하면 O(M log N)
실시간 MST 확장 가능
'''

import heapq

def mst_prim(N, graph):
    visited = [False] * (N+1)
    heap = [(0, 1)]  # (비용, 정점)
    total = 0

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += cost

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))

    return total

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향

print(mst_prim(N, graph))