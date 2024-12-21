def solution(board, h, w):
    n = len(board)
    direction = (
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    )
    answer = 0
    
    for k in range(4):
        h_check = h + direction[k][0]
        d_check = w + direction[k][1]
        if 0<= h_check < n and 0 <= d_check < n:
            if board[h][w] == board[h_check][d_check]:
                answer += 1
    return answer