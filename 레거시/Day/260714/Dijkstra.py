from collections import defaultdict
import heapq

n, m = map(int, input().split())
INF = float('inf')
graph = defaultdict(list)
for _ in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

distances = [INF] * (n+1)
path = [-1] * (n+1)

hq = [(0,1)]
path[1] = 0
distances[1] = 0



while hq:
    weight, node = heapq.heappop(hq)
    if distances[node] < weight:
        continue

    for nxt_node, w in graph[node]:
        next_weight = w + weight
        if distances[nxt_node] > next_weight:
            distances[nxt_node] = next_weight
            path[nxt_node] = node
            heapq.heappush(hq, (next_weight, nxt_node))

result = []
p = n
if distances[n] == INF:
    print(-1)
else:
    while p != 0:
        result.append(p)
        p = path[p]
    result.reverse()
    print(*result)

