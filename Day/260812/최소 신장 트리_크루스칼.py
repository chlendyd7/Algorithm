#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS26fKIucDFAVT&categoryId=AWUS26fKIucDFAVT&categoryType=CODE&problemTitle=%EC%B5%9C%EC%86%8C+%EC%8B%A0%EC%9E%A5+%ED%8A%B8%EB%A6%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
import heapq


def solution():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w,e))
        graph[e].append((w,s))

    visited = [False] * (V+1)
    cnt = 0
    total_weight = 0
    hq = [(0,0)]

    while hq:
        weight, node = heapq.heappop(hq)
        if visited[node]:
            continue
        
        total_weight += weight
        cnt += 1
        visited[node] = True

        if cnt == V+1:
            break

        for next_w, next_node in graph[node]:
            heapq.heappush(hq, (next_w, next_node))

    return total_weight

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')