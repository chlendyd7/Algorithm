from collections import defaultdict

def solution(a, edges):
    # 1. a의 총합이 0인지 확인
    if sum(a) != 0:
        return -1
    
    # 2. 그래프 구성
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 3. DFS로 리프 노드부터 처리
    visited = [False] * len(a)
    total_moves = 0
    
    def dfs(node):
        nonlocal total_moves
        visited[node] = True
        current_sum = a[node]
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                # 자식 노드 처리
                child_sum = dfs(neighbor)
                current_sum += child_sum
                total_moves += abs(child_sum)
        
        return current_sum
    
    # 루트 노드(0번)에서 시작
    dfs(0)
    return total_moves
