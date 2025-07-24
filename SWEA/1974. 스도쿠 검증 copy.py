def solution(board):
    for i in range(9):
        row_set = set()
        col_set = set()
        subgrid_set = set()
        
        start_row = (i // 3) * 3
        start_col = (i % 3) * 3

        for j in range(9):
            row_set.add(board[i][j])
            col_set.add(board[j][i])
            sub_row = start_row + j // 3
            sub_col = start_col + j % 3
            subgrid_set.add(board[sub_row][sub_col])
    
    if len(row_set) != 9 or len(col_set) != 9 or len(subgrid_set) != 9:
        return 0

    return 1


T = int(input())
for t in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    print(solution(board))
