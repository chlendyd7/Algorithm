from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph[1])
    visited = [-1] * (n+1)
    q = deque([1])
    visited[1] = 1
    
    while q:
        now = q.popleft()
        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                q.append(node)
    
    max_node = max(visited)
                
    return visited.count(max_node)
