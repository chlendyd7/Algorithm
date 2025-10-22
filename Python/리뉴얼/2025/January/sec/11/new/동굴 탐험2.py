from collections import deque


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    orders = [0 for _ in range(n)]
    for a, b in order:
        orders[b] = a

    visited = [False for _ in range(n)]
    q = deque([0])

    after = dict()
    
    while q:
        now = q.popleft()

        if orders[now] and not visited[orders[now]]:
            after[orders[now]] = now
            continue

        visited[now] = True
        for next_node in graph[now]:
            if not visited[next_node]:
                q.append(next_node)
        
        if now in after:
            q.append(after[now])
    
    return all(visited)
