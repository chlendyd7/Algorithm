'''
    info[i] 는 i번 노드에 있는 양 또는 늑대
    0은 양, 1은 늑대
    info[0]의 값은 항상 0

    edges = [부모노드, 자식노드] 서로 연결된 두 노드를 나타냄
'''
from collections import defaultdict, deque


def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    print(graph)    
    max_sheep= 0
    q = deque([(0, 0, 0, [])])

    while q:
        current, sheep, wolves, next_nodes = q.popleft()

        if info[current] == 0:
            sheep += 1
        else:
            wolves += 1
        
        if sheep <= wolves:
            continue
            
        max_sheep = max(max_sheep, sheep)
        
        next_nodes = next_nodes + graph[current]
        for next_node in next_nodes:
            q.append((next_node, sheep, wolves, [n for n in next_nodes if n != next_node]))

    
    return max_sheep
solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])


def solution(info):
    from collections import deque
    
    n = len(info)
    
    # 트리 구성
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        parent = info[i]
        graph[parent].append(i)
    
    # BFS: (현재_노드, 방문한_노드_set, 양, 늑대)
    queue = deque([(0, {0}, 1, 0)])
    visited = set()
    max_sheep = 0
    
    while queue:
        node, visited_nodes, sheep, wolf = queue.popleft()
        
        # 상태 중복 체크 (현재 노드 + 방문한 노드들)
        state = (node, frozenset(visited_nodes), sheep, wolf)
        if state in visited:
            continue
        visited.add(state)
        
        max_sheep = max(max_sheep, sheep)
        
        # 방문 가능한 모든 노드 탐색
        for next_node in get_available_nodes(node, visited_nodes, graph):
            new_visited = visited_nodes | {next_node}
            is_sheep = info[next_node] == 0
            
            new_sheep = sheep + (1 if is_sheep else 0)
            new_wolf = wolf + (0 if is_sheep else 1)
            
            # 양 ≥ 늑대 조건 확인
            if new_sheep >= new_wolf:
                queue.append((next_node, new_visited, new_sheep, new_wolf))
    
    return max_sheep

def get_available_nodes(current, visited_nodes, graph):
    # 현재 노드에서 갈 수 있는 노드들
    # = 방문한 노드들의 자식 중 아직 방문하지 않은 노드
    available = set()
    for node in visited_nodes:
        for child in graph[node]:
            if child not in visited_nodes:
                available.add(child)
    return available
