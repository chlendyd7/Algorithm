

import heapq
import sys


def solution(start):
    
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for next in graph[now]:
            cost = d + next[1]
            if cost < dis[next[0]]:
                dis[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return dis[n]

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dis = [sys.maxsize] * (n+1)

print(solution(1))
