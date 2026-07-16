from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # 방문 여부 및 거리를 기록할 배열 (-1로 초기화)
    visited = [-1] * (n + 1)
    
    # 1번 노드 시작 설정
    queue = deque([1])
    visited[1] = 0
    
    while queue:
        curr = queue.popleft()
        
        for nxt in graph[curr]:
            # 아직 방문하지 않은 노드라면 현재 거리 + 1로 방문 처리
            if visited[nxt] == -1:
                visited[nxt] = visited[curr] + 1
                queue.append(nxt)
                
    # 가장 먼 거리 찾기
    max_dist = max(visited)
    
    # 가장 먼 거리에 있는 노드의 개수 세기
    return visited.count(max_dist)
