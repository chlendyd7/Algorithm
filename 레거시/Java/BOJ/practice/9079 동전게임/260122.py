
from collections import deque


flips = [
    [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], # 행
    [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], # 열
    [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]                         # 대각선
]

def check(board):
    num = board[0][0]
    for i in range(3):
        for j in range(3):
            if board[i][j] != num:
                return False
    return True

def change(board, flip):
    new_board = [row[:] for row in board]
    for x,y in flip:
        new_board[x][y] = not new_board[x][y]
    return new_board

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

T = int(input())
for _ in range(T):
    board = []
    for _ in range(3):
        inputs = input().split()
        temp = []
        for i in inputs:
            if i == 'H':
                temp.append(True)
            else:
                temp.append(False)
        board.append(temp)

    q = deque([(board, 0)])
    visited = set(board_to_tuple(board))
    find = False
    while q:
        curr_board, dist = q.popleft()

        if check(curr_board):
            print(dist)
            find = True
            break

        for flip in flips:
            new_board = change(curr_board, flip)
            tuple_board = board_to_tuple(new_board)
            if tuple_board not in visited:
                q.append((new_board, dist+1))
                visited.add(tuple_board)

    if not find:
        print(-1)
