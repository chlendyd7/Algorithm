import heapq
import sys

# 무한대 값 설정
INF = sys.maxsize

# 다익스트라 함수 정의
def dijkstra(start, graph, N):
    distance = [INF] * (N + 1)  # 시작점에서 각 정점까지의 거리
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # 시작점을 우선순위 큐에 삽입
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:  # 이미 처리된 정점 무시
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    
    return distance

# 입력 받기
N, M, X = map(int, input().split())  # 마을 수, 도로 수, 파티가 열리는 마을 X
graph = [[] for _ in range(N + 1)]  # 그래프 초기화

# 도로 정보 입력
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))  # u에서 v로 가는 시간 t

# 1. 모든 마을에서 X로 가는 최단 경로 계산
to_X = [0] * (N + 1)
for i in range(1, N + 1):
    if i != X:
        to_X[i] = dijkstra(i, graph, N)[X]

# 2. X에서 모든 마을로 가는 최단 경로 계산
from_X = dijkstra(X, graph, N)

# 3. 각 마을에서 파티까지 왕복 시간 계산
max_time = 0
for i in range(1, N + 1):
    round_trip_time = to_X[i] + from_X[i]
    max_time = max(max_time, round_trip_time)

# 결과 출력
print(max_time)
