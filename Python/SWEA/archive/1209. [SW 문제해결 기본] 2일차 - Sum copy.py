def solution():
    board = [list(map(int, input().split())) for _ in range(100)]
    mx_row = 0
    mx_col = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += board[i][j]
            col_sum += board[j][i]
        mx_row = max(row_sum, mx_row)
        mx_col = max(col_sum, mx_col)
    dia = 0
    reverse_dia = 0
    for i in range(100):
        dia += board[i][i]
        reverse_dia += board[i][99-i]

    return max(mx_row, mx_col, dia, reverse_dia)

for t in range(1, 11):
    _ = int(input())
    print(f'#{t} {solution()}')
