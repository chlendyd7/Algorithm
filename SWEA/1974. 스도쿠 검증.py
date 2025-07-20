def solution(board):

    for i in range(9):
        row = [0] * 9
        col = [0] * 9
        for j in range(9):
            if row[board[i][j]] or col[board[j][i]]:
                return 0
            else:
                row[board[i][j]] = 1
                col[board[j][i]] = 1
        

    for i in range(3):
        mat = [0] * 9
        for j in range(3):
            if mat[board[i][j]]:
                return 0

    return 1
        
def solution(board):
    for i in range(9):
        row = [0] * 9
        col = [0] * 9
        for j in range(9):
            if row[board[i][j] - 1] or col[board[j][i] - 1]:
                return 0
            row[board[i][j] - 1] = 1
            col[board[j][i] - 1] = 1

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            check = [0] * 9
            for i in range(3):
                for j in range(3):
                    num = board[box_row + i][box_col + j]
                    if check[num - 1]:
                        return 0
                    check[num - 1] = 1

    return 1


T = int(input())
for t in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    check = solution(board)
