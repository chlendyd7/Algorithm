
from copy import deepcopy


def solution():
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    def check_board(board):
        for w in range(W):
            run = 1
            ok = False
            for d in range(1, D):
                if board[d][w] == board[d-1][w]:
                    run += 1
                else:
                    run = 1
    
                if run >= K:
                    ok = True
                    break
            if not ok:
                return False
        return True

    if K == 1:
        return 0
    if check_board(board):
        return 0

    visited = [0] * D
    def dfs(limit, picked, start, board):
        if picked == limit:
            return check_board(board)

        if D - start < limit - picked:
            return False

        for d in range(start, D):
            if visited[d]:
                continue
            visited[d] = 1
            row_backup = board[d][:]

            board[d] = [0] * W
            if dfs(limit, picked + 1, d + 1, board):
                return True
            board[d] = [1] * W
            if dfs(limit, picked + 1, d + 1, board):
                return True

            board[d] = row_backup
            visited[d] = 0
        return False

    for length in range(1, D+1):
        tmp_board = deepcopy(board)
        if dfs(length, 0, 0, tmp_board):
            return length

T = int(input())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')
