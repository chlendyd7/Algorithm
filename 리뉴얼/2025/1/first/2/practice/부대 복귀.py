from collections import deque


def solution(n, roads, sources, destination):

    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    Q = deque([destination])
    visited[destination] = 0
    while Q:
        now = Q.popleft()
        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                Q.append(node)
    return [visited[i] for i in sources]
