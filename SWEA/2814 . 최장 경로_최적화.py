def dfs(node, cnt, visited, graph):
    global max_len
    max_len = max(max_len, cnt)
 
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, cnt+1, visited, graph)
            visited[next_node] = False
 
 
 
T = int(input())
 
for t in range(1,T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
 
    for m in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
 
    max_len = 0
    for i in range(1, N+1):
        visited = [False] * (N+1)
        visited[i] = True
        dfs(i, 1, visited, graph)
 
    print(f"#{t} {max_len}")