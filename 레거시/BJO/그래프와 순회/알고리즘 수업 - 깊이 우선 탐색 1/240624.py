import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

def DFS(start):
    stack = [start]
    visited = [-1] * (N+1)
    result = [0] * (N+1)
    cnt = 1
    
    while stack:
        cnt_node = stack.pop()
        
        if visited[cnt_node] == 1:
            continue
        
        visited[cnt_node] = 1
        result[cnt_node] = cnt
        cnt+=1
        
        for node in graph[cnt_node]:
            if visited[node] == -1:
                stack.append(node)
    return result

result = DFS(R)

print(*result[1:], sep='\n')
