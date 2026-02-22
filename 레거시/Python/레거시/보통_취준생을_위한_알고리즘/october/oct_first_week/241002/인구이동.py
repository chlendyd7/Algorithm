from collections import deque
import sys

def check(col, row):
    return 0 <= col < N and 0<= row < N

def bfs(x,y):
    q.append((x,y))
    union = []
    union.append((x,y))
    while q:
        a,b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if check(na, nb) and visitied[na][nb] == 0:
                if L <= abs(pan[na][nb] - pan[a][b]) <= R:
                    visitied[na][nb] = 1
                    q.append((na,nb))
                    union.append((na,nb))
    if len(union) <= 1:
        return 0
    result = sum(pan[a][b] for a,b in union) // len(union)
    for a,b in union:
        pan[a][b] = result
    return 1





N, L, R = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

day = 0
while True:
    stop = 0
    visitied = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visitied[i][j] == 0:
                visitied[i][j] = 1
                stop += bfs(i,j)
    if stop == 0:
        break
    day += 1
print(day)
