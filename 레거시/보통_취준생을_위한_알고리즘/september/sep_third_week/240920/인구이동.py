from collections import deque
import sys
N, L, R = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
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
            if 0<= na < N and 0<= nb < N and not visited[na][nb]:
                if L<= abs(pan[a][b] - pan[na][nb]) <= R:
                    visited[na][nb] = 1
                    q.append((na,nb))
                    union.append((na,nb))
    if len(union) <= 1:
        return False
    result = sum(pan[a][b] for a,b in union) // len(union)
    for a,b in union:
        pan[a][b] = result
    return True
    
day = 0
while True:
    stop = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i,j)
    if not stop:
        break
    day += 1
print(day)
