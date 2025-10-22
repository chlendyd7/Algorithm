def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    start_x = -1
    start_y = -1
    found = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start_x, start_y = i, j
                found = True
                break
        if found:
            break


    for ii in range(start_x, N):
        if board[ii][start_y] != 0:  # 0 아닌 곳 만나면 중단
            break
        board[ii][start_y] = 2

    for ii in range(start_x, -1, -1):
        if board[ii][start_y] != 0:
            break
        board[ii][start_y] = 2

    for jj in range(start_y, N):
        if board[start_x][jj] != 0:
            break
        board[start_x][jj] = 2

    for jj in range(start_y, -1, -1):
        if board[start_x][jj] != 0:
            break
        board[start_x][jj] = 2

    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
