# https://school.programmers.co.kr/learn/courses/30/lessons/72413
import heapq
import sys

def solution(n, s, a, b, fares):
    INF = float('inf')
    
    # 2차원 최단 거리 테이블 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로 가는 비용은 0
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    # 간선 정보 입력 (양방향)
    for u, v, w in fares:
        graph[u][v] = w
        graph[v][u] = w
        
    # 플로이드-워셜 알고리즘 수행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    # 최저 택시요금 계산
    # (s -> k) + (k -> a) + (k -> b)
    answer = INF
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])
        
    return answer
