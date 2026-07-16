# https://codeforces.com/problemset/problem/938/D
from collections import defaultdict
import heapq


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w*2))
    graph[b].append((a,w*2))

tickets = list(map(int, input().split()))

distance = [10**18] * (n+1)
hq = []

for i in range(1, n+1):
    distance[i] = tickets[i-1]
    heapq.heappush(hq, (distance[i], i))

while hq:
    dist, now = heapq.heappop(hq)
    
    if distance[now] < dist:
        continue
    
    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(hq, (cost, next_node))

print(*(distance[1:]))
