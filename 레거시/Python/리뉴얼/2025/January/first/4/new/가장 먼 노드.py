from collections import deque, defaultdict

def solution(n, edges):
    # 1. 그래프 초기화
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 2. BFS를 통한 최단 거리 계산
    distances = [-1] * (n + 1)  # 초기 거리: -1 (미방문 상태)
    distances[1] = 0  # 시작 노드의 거리
    queue = deque([1])  # BFS 시작 노드
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 미방문 노드
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    # 3. 가장 먼 노드의 개수 계산
    max_distance = max(distances)
    return distances.count(max_distance)
