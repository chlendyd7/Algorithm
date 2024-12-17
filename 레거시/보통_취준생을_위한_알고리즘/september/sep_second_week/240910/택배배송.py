import heapq
import sys

INF = sys.maxsize

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
graph= [[] for _ in range(n+1)]
dis = [INF]*(n+1)
for _ in range(m):
    start, end, cows = map(int, input().split())
    graph[start].append((end, cows))
    graph[end].append((start, cows))

print(solution(1))
