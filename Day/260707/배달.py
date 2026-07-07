# https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq
from collections import defaultdict

def solution(N, road, K):
    # 그래프 구성
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # Dijkstra 알고리즘
    distances = [float('inf')] * (N + 1)  # 각 노드까지의 최단 거리
    distances[0] = 0  # 더미 노드
    distances[1] = 0  # 시작점
    
    pq = [(0, 1)]  # (거리, 노드)
    
    while pq:
        curr_dist, node = heapq.heappop(pq)
        
        # 이미 최단거리가 확정된 노드면 스킵
        if curr_dist > distances[node]:
            continue
        
        # 인접 노드 탐색
        for next_node, time in graph[node]:
            new_dist = curr_dist + time
            
            # 더 짧은 경로를 찾았다면 업데이트
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    # K 이하의 거리로 도달 가능한 노드 개수
    return sum(1 for d in distances[1:] if d <= K)
