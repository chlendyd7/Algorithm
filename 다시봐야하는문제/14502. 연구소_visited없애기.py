from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empties = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            viruses.append((i, j))
        elif board[i][j] == 0:
            empties.append((i, j))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def spread_virus(walls):
    # 원본 보드 복사
    temp = [row[:] for row in board]
    
    # 벽 설치
    for wx, wy in walls:
        temp[wx][wy] = 1
    
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    
    # 안전 영역 계산
    return sum(row.count(0) for row in temp)

result = 0
walls = []

def dfs(start, depth):
    global result
    if depth == 3:
        result = max(result, spread_virus(walls))
        return

    for i in range(start, len(empties)):
        walls.append(empties[i])
        dfs(i + 1, depth + 1)
        walls.pop()

dfs(0, 0)
print(result)
