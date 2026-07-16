# [0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
from collections import defaultdict, deque


def solution(info, edges):
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)

    answer = 0
    q = deque([(0,0,0,[])])
    while q:
        node, sheep, wolf, next_nodes = q.popleft()
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if sheep <= wolf:
            continue

        answer = max(answer, sheep)
        next_nodes += graph[node]
        for nxt_node in next_nodes:
            q.append((nxt_node, sheep, wolf, [n for n in next_nodes if n != nxt_node]))

    return answer

def solution(info, edges):
    # 1. 인접 리스트 생성
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)
    
    answer = [0]
    
    # 2. 핵심: "현재 갈 수 있는 노드들의 목록"을 상태로 전달
    def dfs(sheep, wolf, available_nodes):
        # 현재 상태에서 양이 더 많으면 최댓값 갱신
        if sheep > wolf:
            answer[0] = max(answer[0], sheep)
        else:
            return  # 늑대가 양을 잡아먹음
        
        # 갈 수 있는 각 노드를 하나씩 시도
        for i, next_node in enumerate(available_nodes):
            # 다음 상태: (현재 목록에서 선택한 노드 제거) + (선택한 노드의 자식 추가)
            new_available = (available_nodes[:i] + 
                           available_nodes[i+1:] + 
                           graph[next_node])
            
            if info[next_node] == 0:  # 양
                dfs(sheep + 1, wolf, new_available)
            else:  # 늑대
                dfs(sheep, wolf + 1, new_available)
    
    # 0번 노드부터 시작 (양 1마리 확보)
    dfs(1, 0, graph[0])
    
    return answer[0]
