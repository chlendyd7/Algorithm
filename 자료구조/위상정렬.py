'''
자료구조.위상정렬의 Docstring
노드 번호(숫자)로 주어지는 방향 그래프
'''

from collections import deque

def topological_sort():
    # v: 노드 개수, e: 간선 개수
    v, e = map(int, input().split())
    
    indegree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        # a번 노드에서 b번 노드로 가는 화살표 (a -> b)
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    
    result = []
    q = deque()
    
    for i in range(1, v+1):
        # 처음 시작 시 진입 차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
    
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    for i in result:
            print(i, end=' ')
        