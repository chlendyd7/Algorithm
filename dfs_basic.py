V,E = map(int, input().split())

def dfs(node):    
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)



graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (V+1)
visited[1] = 1
dfs(1)