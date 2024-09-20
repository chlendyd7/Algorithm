import heapq
import sys


def solution(start):
    q = []
    heapq.heappush(q, (0,start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for next in graph[now]:
            cost = d + next[1]
            if cost < dis[next[0]]:
                dis[next[0]] = cost
                heapq.heappush(q, (cost,next[0]))
    return dis[N]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
dis = [sys.maxsize] * (N+1)

print(solution(1))
