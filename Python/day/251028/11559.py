from collections import deque


RED = 'R'
GREEN = 'G'
BLUE = 'B'
PURPLE = 'P'
YELLOW = 'Y'

N = 12
board = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(row, col, visited):
    q = deque()
    q.append((row, col))
    print(q)
    collections = []
    color = board[row][col]
    visited[row][col] = True

    while q:
        x, y = q.popleft()
        collections.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 12 and 0<= ny < 6 and not visited[nx][ny]:
                if board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))

    return collections


def explode():
    visited = [[False] * 6 for _ in range(12)]
    to_pop = []
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    to_pop.extend(group)
    
    if not to_pop:
        return False

    for x, y in to_pop:
        board[x][y] = '.'
    return True


def apply_gravity():
    for c in range(6):
        stack = []
        for r in range(11, -1, -1):
            if board[r][c] != '.':
                stack.append(board[r][c])
        for r in range(11, -1, -1):
            if stack:
                board[r][c] = stack.pop(0)
            else:
                board[r][c] = '.'

chain = 0
while True:
    if not explode():
        break
    apply_gravity()
    chain += 1

print(chain)