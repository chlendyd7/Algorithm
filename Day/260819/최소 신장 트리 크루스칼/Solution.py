# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS26fKIucDFAVT
from collections import defaultdict
import heapq


def solution():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w,s))
    
    hq = [(0,0)]
    visited = [0] * (V+1)
    cnt = 0
    total_weight = 0

    while hq:
        weight, node = heapq.heappop(hq)
        if visited[node]:
            continue

        if cnt >= V+1:
            break

        total_weight += weight
        visited[node] = True
        cnt += 1

        for next_w, next_n in graph[node]:
            heapq.heappush(hq, (next_w, next_n))

    return total_weight


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
