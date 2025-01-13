from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    condition = defaultdict(int)
    for a, b in order:
        condition[b] = a
    
    after = dict()
    q = deque([0])
    visitied = [False] * n
    

    while q:
        now = q.popleft()
        
        if now in condition and not visitied[condition[now]]:
            after[condition[now]] = now
            continue
        
        for next_node in graph[now]:
            if not visitied[next_node]:
                q.append(next_node)
                visitied[next_node] = True
        
        if now in after:
            q.append(after[now])

    return all(visitied)
