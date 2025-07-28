
from collections import deque


N, M, V = map(int, input().split())
graph = [[0] * (N+1) for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


str = ''
visit = [0] * (N+1)

def dfs(path):
    visit[path] = 1
    print(path, end=' ')
    for i in range(1, N+1):
        if visit[i] == 0 and graph[path][i] == 1:
            dfs(i)

visit = [0] * (N+1)
def bfs(start):
    q = deque()
    q.append(graph[start])
    visit[start] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')

        for i in range(1, N+1):
            if not visit[i] and graph[start][i] == 1:
                q.append(i)
                visit[i] = 1


dfs(V)
bfs(V)
