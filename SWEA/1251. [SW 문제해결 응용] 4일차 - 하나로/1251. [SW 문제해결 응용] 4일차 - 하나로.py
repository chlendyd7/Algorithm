import heapq
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    E = float(input())

    islands = []
    for i in range(N):
        islands.append((x_location[i], y_location[i]))
    
    visited = [False] * N
    min_heap = [(0, 0)]
    total_cost = 0
    count = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
                
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        count += 1

        if count == N:
            break

        x1, y1 = islands[u]
        for v in range(N):
            if not visited[v]:
                x2, y2 = islands[v]
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                heapq.heappush(min_heap, (dist,v))
    
    print(f'#{tc} {round(total_cost * E)}')
