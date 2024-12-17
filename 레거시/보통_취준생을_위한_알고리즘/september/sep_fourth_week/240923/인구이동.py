from collections import deque


n,l,r = map(int,input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    q.append((x,y))
    union = []
    union.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0<= na < n and 0<= nb < n and not visited[na][nb] == 1:
                if l<=abs(maps[na][nb] - maps[a][b]) <= r:
                    visited[na][nb] = 1
                    q.append((na,nb))
                    union.append((na,nb))
    if len(union) <= 1:
        return 0
    result = sum(maps[a][b] for a,b in union) // len(union)
    for a,b in union:
        maps[a][b] = result
    return 1



day = 0
while True:
    stop = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i,j)
    if stop == 0:
        break
    day += 1
print(day)
