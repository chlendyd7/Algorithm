from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(list)
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    condition = defaultdict(int)
    for a, b in order:
        condition[b] = a

    visited = [False] * (n)
    visited[0] = True

    after = {}
    q = deque([0])
    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                if next_node in condition:
                    if not visited[condition[next_node]]:
                        continue
                q.append(next_node)
                visited[next_node] = True
    
    for node in visited:
        if not node:
            return False
    return True
