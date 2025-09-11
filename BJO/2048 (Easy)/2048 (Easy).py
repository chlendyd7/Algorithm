from copy import deepcopy
import os
from pprint import pprint
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


UP = "UP"
DOWN = "DOWN"
RIGHT = "RIGHT"
LEFT = "LEFT"

DIRECTION = [UP, DOWN, RIGHT, LEFT]


def move(dr, board):
    def simulate_stack(stack):
        if stack:
            for k in range(len(stack)-1):
                if stack[k] == stack[k+1]:
                    stack[k] = stack[k]*2
                    stack.pop(k+1)
                    stack.append(0)

        return stack

    #LEFT
    tmp_board = [[0] * N for _ in range(N)]
    if dr == LEFT:
        for r in range(N):
            stack = []
            for c in range(N-1,-1,-1): # N x N
                if board[r][c]: # 숫자가 있으면
                    stack.append(board[r][c])
            stack = simulate_stack(stack)
            for i in range(N):
                tmp_board[r][i] = stack[i]

    if dr == RIGHT:
        for r in range(N):
            stack = []
            for c in range(N):
                if board[r][c]:
                    stack.append(board[r][c])
            stack = simulate_stack(stack)
            i = 0
            for c in range(N-1,-1,-1):
                tmp_board[r][c] = stack[i]
                i+=1

    if dr == DOWN:
        for c in range(N):
            stack = []
            for r in range(N-1,-1,-1):
                if board[r][c]:
                    stack.append(board[r][c])
            i = 0
            stack = simulate_stack(stack)
            for r in range(N-1,-1,-1):
                tmp_board[r][c] = stack[i]
                i+=1

    if dr == UP:
        for c in range(N):
            stack = []
            for r in range(N):
                if board[r][c]:
                    stack.append(board[r][c])
            l_stack = simulate_stack(stack)
            for r in range(N):
                tmp_board[r][c] = l_stack[r]

    return tmp_board

result = 0
def dfs(n, board):
    global result
    
    if n >= 5:
        for i in range(N):
            for j in range(N):
                result = max(result, board[i][j])
        return

    for dr in DIRECTION:
        tmp_board = move(dr, board)
        print(n, dr, 'move_after_board')
        pprint(tmp_board)
        print()
        dfs(n+1, tmp_board)
dfs(0, board)
print(result)
