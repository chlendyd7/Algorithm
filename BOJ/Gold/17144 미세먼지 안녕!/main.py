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
dr = [-1,1,0,0]
dc = [0,0,1,-1]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
r1,c1,r2,c2 = 0, 0, 0, 0
flag = True
for i in range(R):
    if flag:
        for j in range(C):
            if board[i][j] == -1:
                r1 = i
                c1 = j
                flag = False
                break
    else:
        break

r2, c2 = r1+1, c1

def mise(board):
    next_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == -1:
                next_board[r][c] = -1
                continue

            if board[r][c] > 0:
                if board[r][c] > 4:
                    cnt = 0
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < R and 0 <= nc < C:
                            next_board[nr][nc] += int(board[r][c] / 5)
                            cnt += 1
                    next_board[r][c] += board[r][c] - (int(board[r][c] / 5) * cnt)
                else:
                    next_board[r][c] += board[r][c]

    return next_board


direction_up = [(0,1), (-1,0), (0,-1), (1,0)]
direction_down = [(0,1), (1,0), (0,-1), (-1,0)]
def air_condition(board, r1, c1, r2, c2):
    next_board = [[0] * C for _ in range(R)]
    dir = 0
    r, c = r1, c1
    while True:
        nr, nc = r + direction_up[dir][0], c + direction_up[dir][1]
        if 0 > nr or nr >= R or 0 > nc or nr >= C:
            dir += 1
        else:
            if nr == r1 and c == c1:
                break
            next_board[nr][nc] = board[r][c]
            r, c = nr, nc

    dir = 0
    r, c = r2, c2
    while True:
        nr, nc = r + direction_down[dir][0], c + direction_down[dir][1]
        if 0 > nr or nr >= R or 0 > nc or nr >= C:
            dir += 1
        else:
            if nr == r2 and c == c2:
                break
            next_board[nr][nc] = board[r][c]
            r, c = nr, nc

    return next_board


first_step_board = mise(board)
print(first_step_board)
second_step_board = air_condition(first_step_board, r1, c1, r2, c2)
# print(second_step_board)
result = 0
for i in range(R):
    for j in range(C):
        if second_step_board[i][j] == -1:
            continue
        result += second_step_board[i][j]
print(result)