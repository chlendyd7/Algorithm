def trans(board):
    r,c = len(board), len(board[0])
    new_board = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            new_board[j][i] = board[i][j]
    return new_board

from collections import Counter
def op_r(board):
    new_board = []
    max_len = 0
    for row in board:
        new_row = []
        counts = Counter(num for num in row if num != 0)
        sort_pairs = sorted(([num, cnt] for num, cnt in counts.items()), key=lambda x: (x[1], x[0]))
        for num, cnt in sort_pairs:
            new_row.extend((num, cnt))
        max_len = max(max_len, len(new_row))
        new_board.append(new_row)
    for i in range(len(new_board)):
        target = max_len - len(new_board[i])
        new_board[i].extend([0] * target)
    return new_board


def solve():
    R,C,K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(3)]
    R, C = R-1, C-1
    for time in range(101):
        if R < len(board) and C < len(board[0]) and board[R][C] == K:
            print(time)
            return

        if len(board) >= len(board[0]):
            board = op_r(board)
        else:
            board = trans(board)
            board = op_r(board)
            board = trans(board)

    print(-1)
    
solve()