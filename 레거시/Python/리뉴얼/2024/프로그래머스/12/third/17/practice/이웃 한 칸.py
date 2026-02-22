def solution(board, h, w):
    n = len(board)
    count = 0
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    
    for k in range(4):
        nx = dx[k] + h
        ny = dy[k] + w
        if 0<= nx < n and 0<= ny < h:
            if board[h][w] == board[nx][ny]:
                count += 1
    return count
