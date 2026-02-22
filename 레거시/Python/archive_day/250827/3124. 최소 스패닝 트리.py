from collections import defaultdict
import heapq


def solution():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b, cost = map(int, input().split())
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    visited = [0] * (V+1)
    heap = [(0, 1)]
    total = 0

    while heap:
        cost, now = heapq.heappop(heap)
        if visited[now]:
            continue
        visited[now] = True
        total += cost

        for cost, next in graph[now]:
            if not visited[next]:
                heapq.heappush(heap, (cost, next))
    return total

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
