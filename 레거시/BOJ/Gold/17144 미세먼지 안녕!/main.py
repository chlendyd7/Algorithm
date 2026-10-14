'''
    미세먼지 확산, 인접한 네 방향 공청기 있으면 확산 x Arc/5
    arc - Arc/5 * 확산 방향 갯수
    
    공청기
    윗쪽은 반 시계방향
    아래쪽은 시계방향
    바람이 불면 한칸 이동
    
    공청기 -1
    확산하는 로직 1
    공청기 동작하는 로직 1
    
'''
import copy

dr = [-1,1,0,0]
dc = [0,0,1,-1]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
r1,c1,r2,c2 = 0, 0, 0, 0

up, down = -1, -1
for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i + 1
        break


r2, c2 = r1+1, c1

def mise_spread():
    next_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                amount = board[r][c] // 5
                cnt = 0
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        next_board[nr][nc] += amount
                        cnt += 1
                next_board[r][c] += (board[r][c] - (amount * cnt))
            elif board[r][c] == -1:
                next_board[r][c] = -1
    return next_board

def air_move():
    for i in range(up - 1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(up):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[up][i] = board[up][i-1]
    board[up][1] = 0

    for i in range(down+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, down, -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[down][i] = board[down][i-1]
    board[down][1] = 0

for _ in range(T):
    board = mise_spread()
    air_move()

total_dust = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            total_dust += board[r][c]

print(total_dust)