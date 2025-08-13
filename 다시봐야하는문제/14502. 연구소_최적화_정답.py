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
    visited = [[False] * M for _ in range(N)]
    q = deque()

    # 초기 바이러스 위치
    for vx, vy in viruses:
        q.append((vx, vy))
        visited[vx][vy] = True

    # 벽 설치
    for wx, wy in walls:
        visited[wx][wy] = True  # 벽은 방문 처리

    infected_count = 0
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                infected_count += 1
                q.append((nx, ny))

    return len(empties) - 3 - infected_count

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
