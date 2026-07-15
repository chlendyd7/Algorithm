from collections import defaultdict
import heapq


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b,v = map(int, input().split())
    graph[a].append((b,v*2))
    graph[b].append((a,v*2))

distances = [0] + list(map(int, input().split()))

hq = [(distances[i], i) for i in range(n+1)]
heapq.heapify(hq)
while hq:
    w, node = heapq.heappop(hq)
    if distances[node] < w:
        continue
    
    for nxt, value in graph[node]:
        cost = w + value
        if cost < distances[nxt]:
            distances[nxt] = cost
            heapq.heappush(hq, (cost, nxt))

print(*distances[1:])