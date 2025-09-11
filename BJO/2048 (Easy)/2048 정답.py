from copy import deepcopy
import sys

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"
DIRECTION = [UP, DOWN, LEFT, RIGHT]

def simulate_stack(stack):
    new_stack = []
    skip = False
    for i in range(len(stack)):
        if skip:
            skip = False
            continue
        if i + 1 < len(stack) and stack[i] == stack[i + 1]:
            new_stack.append(stack[i] * 2)
            skip = True
        else:
            new_stack.append(stack[i])
    return new_stack

def move(dr, board):
    tmp_board = [[0] * N for _ in range(N)]

    # LEFT
    if dr == LEFT:
        for r in range(N): 
            stack = [board[r][c] for c in range(N) if board[r][c] != 0]
            stack = simulate_stack(stack)
            for i in range(len(stack)):
                tmp_board[r][i] = stack[i]

    # RIGHT
    elif dr == RIGHT:
        for r in range(N):
            stack = [board[r][c] for c in range(N-1, -1, -1) if board[r][c] != 0]
            stack = simulate_stack(stack)
            for i in range(len(stack)):
                tmp_board[r][N-1-i] = stack[i]

    # UP
    elif dr == UP:
        for c in range(N):
            stack = [board[r][c] for r in range(N) if board[r][c] != 0]
            stack = simulate_stack(stack)
            for i in range(len(stack)):
                tmp_board[i][c] = stack[i]

    # DOWN
    elif dr == DOWN:
        for c in range(N):
            stack = [board[r][c] for r in range(N-1, -1, -1) if board[r][c] != 0]
            stack = simulate_stack(stack)
            for i in range(len(stack)):
                tmp_board[N-1-i][c] = stack[i]

    return tmp_board

result = 0
def dfs(n, board):
    global result

    if n >= 5:
        result = max(result, max(map(max, board)))
        return

    for dr in DIRECTION:
        tmp_board = move(dr, board)
        dfs(n + 1, tmp_board)

dfs(0, board)
print(result)
