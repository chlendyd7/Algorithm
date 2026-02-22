'''
    N번만 쏠 수 있음
    W x H
    구슬은 좌 우로만 움직임 맨 위에 있는 벽돌
    명중한 벽돌은 상하좌우 -1칸 만큼 같이 제거
    제거되는 점위 내에 있는 벽돌은 동시 제거

    빈공간이 있을 경우 벽돌은 밑으로 떨어짐

    남은 벽돌의 개수를 구하라
'''

from collections import deque
from copy import deepcopy
import pprint
import sys
sys.stdin = open('input.txt', 'r')

def find_bukdol(board):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                cnt += 1
    return cnt

def dfs(shoot, now_board):
    # print(f'shoot:{shoot}')
    # pprint.pprint(now_board)
    global result
    tmp = find_bukdol(now_board)
    if not tmp:
        result = min(result, tmp)
        return

    if result == 0:
        return

    if shoot == N:
        result = min(result, tmp)
        # print(result, 'findbukdol:', tmp)
        return

    for col in range(W):
        # print('col:', col)
        tmp_board = None
        for row in range(H):
            if now_board[row][col]:
                tmp_board = simulater([row,col], now_board)
                break
        if tmp_board:
            dfs(shoot+1, tmp_board)
    
    # if not tmp_board:
    #     result = 0
    #     return




def simulater(first_idx, now_board):
    tmp_board = deepcopy(now_board)
    DIRECTION = [(0,1), (1,0), (-1,0), (0,-1)]
    t_r, t_c = first_idx[0], first_idx[1]
    q = deque([(t_r, t_c, tmp_board[t_r][t_c])])
    while q:
        r, c, cnt = q.popleft()
        for i in range(cnt):
            for dx, dy in DIRECTION:
                nr, nc = r + (dx * i) , c + (dy * i)
                if 0 <= nr < H and 0<= nc < W and tmp_board[nr][nc]:
                    q.append((nr, nc, tmp_board[nr][nc]))
                    tmp_board[nr][nc] = 0

    tmp_board = down_simulater(tmp_board)
    return tmp_board

def down_simulater(now_board):
    for col in range(W):
        stack = []
        for row in range(H-1, -1, -1):
            if now_board[row][col]:
                stack.append(now_board[row][col])
        
        for row in range(H-1, -1, -1):
            if stack:
                now_board[row][col] = stack.pop(0)
            else:
                now_board[row][col] = 0

    # print('down_simulater:', now_board)
    return now_board

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    result = 1e9

    dfs(0, board)
    print(f'#{tc} {result}')
