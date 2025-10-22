from collections import defaultdict

def solution():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (N+1)
    
    def dfs(node, visited):
        visited[node] = 1
        for next in graph[node]:
            if visited[next]:
                continue
            dfs(next, visited)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            dfs(i, visited)

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')