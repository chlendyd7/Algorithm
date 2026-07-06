# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(com_idx):
        visited[com_idx] = True
        
        for neighbor_idx in range(n):
            if computers[com_idx][neighbor_idx] == 1 and not visited[neighbor_idx]:
                dfs(neighbor_idx)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
                
    return answer

def solution(n, computers):
    # 처음에는 자기 자신이 부모(독립된 그룹)
    parent = [i for i in range(n)]
    
    # 특정 컴퓨터가 속한 그룹의 '대표(루트 노드)'를 찾는 함수
    def find(x):
        if parent[x] == x:
            return x
        # 경로 압축 (탐색 속도를 높이기 위해 부모를 루트로 바로 갱신)
        parent[x] = find(parent[x])
        return parent[x]
    
    # 두 컴퓨터의 그룹을 하나로 합치는 함수
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x # y 그룹을 x 그룹 아래로 합침

    # 모든 연결 관계를 보며 합치기 수행
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)
                
    # 모든 컴퓨터의 최종 대표(루트)를 찾아서 그 종류의 개수를 세기
    # (주의: 최종적으로 find를 한번씩 다 거쳐야 완전히 동기화됩니다.)
    unique_networks = set(find(i) for i in range(n))
    
    return len(unique_networks)