from collections import deque


flips = [
    [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], # 행
    [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], # 열
    [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]                         # 대각선
]
def check(board):
    coin = board[0][0]
    for i in range(3):
        for j in range(3):
            if board[i][j] != coin:
                return False
    return True

def flip_board(board, cells):
    new_board = [row[:] for row in board]
    for r, c in cells:
        new_board[r][c] = 'T' if new_board[r][c] == 'H' else 'H'
    return new_board

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

T = int(input())
for _ in range(T):
    board = [input().split() for _ in range(3)]
    start_state = board_to_tuple(board)
    q = deque([(board,0)])
    visited = {start_state}
    found = False
    
    while q:
        curr_board, dist = q.popleft()
        
        if check(curr_board):
            print(dist)
            found = True
            break

        for cells in flips:
            next_board = flip_board(curr_board, cells)
            next_state = board_to_tuple(next_board)
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_board, dist+1))

    if not found:
        print(-1)

