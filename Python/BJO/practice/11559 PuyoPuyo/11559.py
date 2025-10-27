'''
    아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다
    1연쇄 -> 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다
    차례대로 아래로 떨어지게 된다
    R,G,B,P,Y
    
'''
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

def bfs(x, y, color, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    connected = [(x,y)]
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    connected.append((nx,ny))
    return connected


def explode():
    visited = [[False] * 6 for _ in range(12)]
    to_pop = []
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, board[i][j], visited)
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