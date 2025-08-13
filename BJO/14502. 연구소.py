from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

'''
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
0은 빈칸 1은 벽 2는 바이러스
'''

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

viruses = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            viruses.append((i,j))
result = 0

def calculate_virus(board):
    temp = deepcopy(board)
    direction = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]
    q = deque(viruses)
    while q:
        i,j = q.popleft()
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))

    return sum(row.count(0) for row in temp)


def dfs(wall_cnt, board):
    global result
    if wall_cnt == 3:
        result = max(result, calculate_virus(board))
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(wall_cnt + 1, board)
                board[i][j] = 0


dfs(0, board)
print(result)