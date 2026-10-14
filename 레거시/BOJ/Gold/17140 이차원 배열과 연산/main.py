'''
    R연산 행에 정렬, 행의 개수 >= 열의 개수인 경우 적용
    c연산 행의 개수 < 열의 개수
'''
from collections import Counter
def op_r(board):
    new_board = []
    max_len = 0
    
    for row in board:
        counts = Counter(num for num in row if num != 0)
        sorted_pairs = sorted(counts.items(), key=lambda x: (x[1], x[0]))
        
        new_row = []
        for num, cnt in sorted_pairs:
            new_row.extend([num, cnt])
            if len(new_row) >= 100: break
        
        new_board.append(new_row)
        max_len = max(max_len, len(new_row))
    
    for i in range(len(new_board)):
        padding_size = max_len - len(new_board[i])
        new_board[i].extend([0] * padding_size)

    return new_board

def transpose(board):
    rows = len(board)
    cols = len(board[0])
    
    new_board = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            new_board[c][r] = board[r][c]
    return new_board

def solve():
    R, C, K = map(int, input().split())
    R, C = R-1, C-1
    board = [list(map(int, input().split())) for _ in range(3)]
    for time in range(101):
        if R < len(board) and C < len(board[0]):
            if R < len(board) and C < len(board[0]):
                if board[R][C] == K:
                    print(time)
                    return
        row_count = len(board)
        col_count = len(board[0])

        if row_count >= col_count:
            board = op_r(board)
        else:
            board = transpose(board) # 직접 만든 함수로 뒤집기
            board = op_r(board)      # 행 연산 함수 재활용
            board = transpose(board) # 다시 원래대로 뒤집기

    print(-1)

solve()