def solution():
    board = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        row_set = set()
        col_set = set()
        
        for j in range(9):
            row_set.add(board[i][j])
            col_set.add(board[j][i])
    

        if len(row_set) != 9 or len(col_set) != 9:
            return 0

    for i in range(0, 9, 3):  # row 시작점
        for j in range(0, 9, 3):  # col 시작점
            grid_set = set()
            for x in range(3):
                for y in range(3):
                    grid_set.add(board[i + x][j + y])
            if len(grid_set) != 9:
                return 0

    return 1


T = int(input())
for t in range(1, T+1):
    print(solution())
