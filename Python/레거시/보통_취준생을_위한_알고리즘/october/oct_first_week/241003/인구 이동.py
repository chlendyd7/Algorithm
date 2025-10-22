from collections import deque


def check(row, col):
    return 0<= row < N and 0<= col < N

dx = [1,0,-1,0]
dy = [0,1,0,-1]



def bfs(x, y):
    q = deque()
    q.append([x,y])
    union = []
    union.append([x,y])

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if check(nx,ny) and not visited[nx][ny]:
                if L<= abs(board[nx][ny] - board[x][y]) <= R:
                    union.append([nx,ny])
                    q.append([nx,ny])
                    visited[nx][ny] = 1
    if len(union) > 1:
        union_result = sum(board[x][y] for x,y in union) // len(union)
        for x,y in union:
            board[x][y] = union_result
        return 1

    elif len(union) == 1:
        return 0

N, L, R = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
union = []

day = 0
while True:
    work = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                work += bfs(i,j)
    if not work:
        break
    day += 1
print(day)
