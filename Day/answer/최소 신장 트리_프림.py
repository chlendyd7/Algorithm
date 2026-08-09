#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS26fKIucDFAVT&categoryId=AWUS26fKIucDFAVT&categoryType=CODE&problemTitle=%EC%B5%9C%EC%86%8C+%EC%8B%A0%EC%9E%A5+%ED%8A%B8%EB%A6%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


import heapq


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph =[[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))
    
    visited = [False] * (V+1)
    pq = [(0,0)]
    
    total_weight = 0
    cnt = 0
    while pq:
        w, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_weight += w
        cnt += 1
        
        if cnt == V+1:
            break
        
        for next_w, next_v in graph[u]:
            if not visited[next_v]:
                heapq.heappush(pq, (next_w, next_v))

print(f'#{t} {total_weight}')
