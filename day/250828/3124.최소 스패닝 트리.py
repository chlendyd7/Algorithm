from collections import defaultdict
import heapq


from collections import defaultdict
import heapq

def solution():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    visited = [0] * (V + 1)
    heap = [(0, 1)]   # (비용, 노드) 시작은 임의의 노드 1
    total = 0

    while heap:
        cost, now = heapq.heappop(heap)

        # 이미 MST에 포함된 노드면 무시
        if visited[now]:
            continue

        # 지금 꺼낸 노드를 MST에 포함시키고 비용 더함
        visited[now] = 1
        total += cost

        # 인접 간선들을 힙에 넣음
        for nxt, n_c in graph[now]:
            if not visited[nxt]:
                heapq.heappush(heap, (n_c, nxt))

    return total


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')