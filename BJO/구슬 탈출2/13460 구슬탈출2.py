'''
    빨간 구슬과 파란 구슬을 넣은 뒤 빨간 구슬을 구멍을 통해 빼냄
    N, M 크기 구멍은 하나만 있음
    파란 구슬이 구멍에 들어가면 안됨
    
    왼쪽 기울이기, 오른쪽 기울이기, 위쪽 기울이기, 아랜쪽 기울이기
    동시에 구멍 x, 같은 칸x, 모두 한 칸을 차지
    기울이기 동작을 그만 하는것은 더 이상 구슬이 움직이지 않을 때
    최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하시오

    N, M 크기
    .은 빈칸 #은 장애물 o는 구멍 R은 빨간 구슬 B는 파란 구슬
    크기는 10x10 100
    10번 이하로 움직이기 안되면 -1


    백트래킹
        각 방향으로 기울이기
        장애물 만날 때 까지
        시뮬레이션 진행

    순서가 방향에 따른 빨간공, 파란공의 index 좌표에 따라 진행
    먼저 이동시키고 그 뒤 이동시키기

    '''

from copy import deepcopy
from pprint import pprint
import sys


N, M = map(int, input().split())
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
BLUE = 'B'
RED = 'R'

DIRECTION = {
    UP: (-1,0), #상
    DOWN: (1,0), #하
    LEFT: (0,-1), #좌
    RIGHT: (0,1) #우
}

red = blue = hole = (0,0)
board = []
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'R':
            red = (i,j)
        if row[j] == 'B':
            blue = (i,j)
        if row[j] == 'O':
            hole = (i,j)
    board.append(row)

result = 11
def dfs(cnt, board, red, blue):

    global result
    if cnt > 10:
        # print(red, blue)
        return

    # 같이 들어가 있어도 return
    if blue == hole:
        print('hall in blue')
        return

    if red == hole:
        print('result:', cnt)
        result = min(result, cnt)
        return

    #시뮬레이션 돌려서 board 바꿔주기
    tmp_board = deepcopy(board)
    for dr in DIRECTION.keys():
        s_red, s_blue = simulator(tmp_board, red, blue, dr)
        dfs(cnt+1, tmp_board, s_red, s_blue)


def simulator(board, red, blue, dr):
    # 위치 비교해서 먼저 굴릴 공 찾기
    rr, rc = red
    br, bc = blue

    if dr == UP:
        if br < rr: #blue가 더 위면 블루부터
            red, blue = simulator_first(board, red, blue, UP, BLUE)
        else:
            red, blue = simulator_first(board, red, blue, UP, RED)

    if dr == DOWN:
        if br > rr: #blue 가 더 아래면
            red, blue = simulator_first(board, red, blue, UP, BLUE)
        else:
            red, blue = simulator_first(board, red, blue, UP, RED)
            
    if dr == LEFT:
        if bc < rc:
            red, blue = simulator_first(board, red, blue, UP, BLUE)
        else:
            red, blue = simulator_first(board, red, blue, UP, RED)

    if dr == RIGHT:
        if bc > rc:
            red, blue = simulator_first(board, red, blue, UP, BLUE)
        else:
            red, blue = simulator_first(board, red, blue, UP, RED)

    return red, blue

def simulator_first(board, red, blue, dir, first):
    if first == RED:
        red = ball_simulator(board, red[0], red[1], dir, RED)
        blue = ball_simulator(board, blue[0], blue[1], dir, BLUE)
    else:
        red = ball_simulator(board, blue[0], blue[1], dir, BLUE)
        blue = ball_simulator(board, red[0], red[1], dir, RED)

    return red, blue


def ball_simulator(board, sr, sc, dir, color):
    board[sr][sc] = '.'
    dr, dc = DIRECTION[dir]
    r, c = sr, sc
    while True:
        nr, nc = r + dr, c + dc
        if board[nr][nc] == '.':  # 내가 있는 곳이 길이면
            r, c = nr, nc
        elif board[nr][nc] == 'O':
            r, c = nr, nc
            break
        else: #벽, 다른 구슬 만나면
            break

    board[r][c] = color
    return (r,c)

print(red, blue)
dfs(0, board, red, blue)
print(result)