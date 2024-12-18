def solution(board, h, w):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    n = len(board)
    count = 0

    for k in range(4):
        nx = dx[k] + h
        ny = dy[k] + w
        if 0<= nx < n and 0<= ny < n:
            if board[h][w] == board[nx][ny]:
                count += 1
    return count
