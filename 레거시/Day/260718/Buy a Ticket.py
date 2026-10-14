# https://codeforces.com/problemset/problem/938/D
from collections import defaultdict
import heapq


n,m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c*2))
    graph[b].append((a,c*2))

answer = [0] + list(map(int, input().split()))
hq = []
for i, w in enumerate(answer):
    heapq.heappush(hq, (w,i))

while hq:
    w, node = heapq.heappop(hq)
    
    if answer[node] < w:
        continue

    for nxt_node, nxt_weight in graph[node]:
        if answer[nxt_node] >  w + nxt_weight:
            heapq.heappush(hq, (w+nxt_weight, nxt_node))
            answer[nxt_node] = w + nxt_weight

print(*answer[1:])
