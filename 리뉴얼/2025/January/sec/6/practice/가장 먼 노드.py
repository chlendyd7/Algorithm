from collections import defaultdict, deque


def solution(n, edge):
    node_dict = defaultdict(list)
    for a,b in edge:
        node_dict[a].append(b)
        node_dict[b].append(a)
    visited = [-1] * (n+1)
    
    q = deque([1])
    visited[1] = 0

    while q:
        now = q.popleft()
        for node in node_dict[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                q.append(node)

    max_cnt = max(visited)
    return visited.count(max_cnt)
