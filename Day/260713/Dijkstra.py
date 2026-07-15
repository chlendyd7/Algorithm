#https://codeforces.com/problemset/problem/20/C
from collections import defaultdict
import heapq

INF = 10**18
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [1e9] * (n+1)
parent = [0] * (n+1)
hq = [(0, 1)]
distance[1] = 0

while hq:
    dist, node = heapq.heappop(hq)
    if distance[node] < dist:
        continue

    for n_node, value in graph[node]:
        n_dist = value + dist
        if distance[n_node] > n_dist:
            distance[n_node] = n_dist
            heapq.heappush(hq, (n_dist, n_node))
            parent[n_node] = node


if distance[n] == 1e9:
    print(-1)
else:
    path = []
    cur = n

    while cur != 0:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    print(*path)