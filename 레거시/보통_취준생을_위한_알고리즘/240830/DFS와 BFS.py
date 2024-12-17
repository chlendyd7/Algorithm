from collections import deque


n,m,v = map(int,input().split())
vertex =[[0] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    vertex[a][b] = vertex[b][a] = 1

visit = [0] * (n+1)

def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if visit[i] == 0 and vertex[v][i] == 1:
            dfs(i)

def bfs(v):
    visit[v] = 0
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i]==1 and vertex[v][i] == 1:
                q.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)
