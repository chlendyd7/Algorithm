from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(list)
    for a,b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    condition = defaultdict(int)
    for a, b in order:
        condition[b] = a
    
    visited = [False] * n
    q = deque([0])
    after = dict()
    
    while q:
        now = q.popleft()
        
        if now in condition and not visited[condition[now]]:
            after[condition[now]] = now
            continue
        
        visited[now] = True
        
        for next_node in graph[now]:
            if not visited[next_node]:
                q.append(next_node)

        if now in after:
            q.append(after[now])
    return all(visited)