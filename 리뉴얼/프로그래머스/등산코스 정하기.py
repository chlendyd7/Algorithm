import heapq
from collections import defaultdict
import sys

def solution(n, paths, gates, summits):
    # 그래프 생성
    graph = defaultdict(list)
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 정상(summit)을 set으로 변환 (빠른 탐색 위해)
    summit_set = set(summits)

    # 우선순위 큐를 활용한 다익스트라
    def dijkstra():
        intensity = [sys.maxsize] * (n + 1)
        pq = []
        
        # 모든 출입구(gates)에서 시작
        for gate in gates:
            heapq.heappush(pq, (0, gate))  # (현재 intensity, 현재 노드)
            intensity[gate] = 0
        
        while pq:
            current_intensity, node = heapq.heappop(pq)
            
            # 방문한 노드의 intensity가 더 크면 무시
            if current_intensity > intensity[node]:
                continue
            
            # 인접 노드 탐색
            for neighbor, cost in graph[node]:
                max_intensity = max(current_intensity, cost)
                
                # intensity가 더 적은 경우만 갱신
                if max_intensity < intensity[neighbor]:
                    intensity[neighbor] = max_intensity
                    # 정상인 경우에는 더 탐색하지 않음
                    if neighbor not in summit_set:
                        heapq.heappush(pq, (max_intensity, neighbor))
        
        return intensity
    
    # 최소 intensity 계산
    intensity = dijkstra()

    # 정상 중 최소 intensity 선택
    answer = []
    for summit in sorted(summits):  # 정상 번호가 작은 것부터 확인
        answer.append((intensity[summit], summit))
    
    # intensity 기준으로 최소값 선택
    answer.sort()
    return [answer[0][1], answer[0][0]]
