'''
오른쪽 한 칸 이동
땅과 가장 가까운 상어를 잡음
상어가 이동

상어이동: 칸
경계를 넘는 경우 반대로 바꿔서 속력 유지 이동
같은 칸이면 가장 큰 상어가 모두 잡아먹음
R,C, M(상어 수)
r,c,s,d,z
rc위치, s속력, d는이동방향, z는 크기

딕셔너리로 관리 가능 할 듯?

'''
direction = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]
        
R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in (1,2):
        s = s % (2 * R - 2)
    else:
        s = s % (2 * C -2)
    board[r-1][c-1] = [s,d,z]
    print(s)

people = 0
cnt = 0
def move(board):
    new_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                s, d, z = board[r][c]
                curr_r, curr_c, curr_d = r, c, d

                for _ in range(s):
                    dr, dc = direction[curr_d]
                    nr, nc = curr_r + dr, curr_c + dc

                    if not (0 <= nr < R and 0 <= nc < C):
                        if curr_d == 1: curr_d = 2
                        elif curr_d == 2: curr_d = 1
                        elif curr_d == 3: curr_d = 4
                        elif curr_d == 4: curr_d = 3

                        dr, dc = direction[curr_d]
                        nr, nc = curr_r + dr, curr_c + dc
                    curr_r, curr_c = nr, nc
                if new_board[curr_r][curr_c]:
                    if z > new_board[curr_r][curr_c][2]:
                        new_board[curr_r][curr_c] = [s, curr_d, z]
                else:
                    new_board[curr_r][curr_c] = [s, curr_d, z]
    return new_board


for people in range(C):
    for r in range(R):
        if board[r][people]:
            cnt += board[r][people][2]
            board[r][people] = 0
            break
    board = move(board)
    people += 1

print(cnt)
