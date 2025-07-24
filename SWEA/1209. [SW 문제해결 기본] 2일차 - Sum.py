def solution():
    board = [list(map(int, input().split()))]
    max_row = [0] * 100
    col_sum = [0] * 100
    dia = 0
    reverse_dia = 0

    for i in range(100):
        max_row[i] = sum(board[i])
        dia += board[i][i]
        reverse_dia += board[i][99-i]
        for j in range(100):
            col_sum[j] += board[i][j]
        
    return max(max(max_row), max(col_sum), dia, reverse_dia)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
