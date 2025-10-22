from copy import deepcopy
import sys

N, M = map(int, sys.stdin.readline().split())
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
BLUE = 'B'
RED = 'R'

DIRECTION = {
    UP: (-1, 0),   # 상
    DOWN: (1, 0),  # 하
    LEFT: (0, -1), # 좌
    RIGHT: (0, 1)  # 우
}

red = blue = hole = (0, 0)
board = []
for i in range(N):
    row = list(sys.stdin.readline().strip())
    for j in range(M):
        if row[j] == 'R':
            red = (i, j)
        if row[j] == 'B':
            blue = (i, j)
        if row[j] == 'O':
            hole = (i, j)
    board.append(row)

result = 11
visited = set()


def dfs(cnt, board, red, blue):
    global result

    # 방문 체크
    state = (red, blue)
    if state in visited:
        return
    visited.add(state)

    # 이미 찾은 최소값보다 크거나 같으면 탐색 중단
    if cnt >= result:
        return

    # 10번 이상 기울이면 실패
    if cnt > 10:
        return

    # 파란 구슬이 구멍에 들어간 경우 실패
    if blue == hole:
        return

    # 빨간 구슬이 구멍에 들어가면 성공
    if red == hole:
        result = min(result, cnt)
        return

    # 4방향으로 기울이기
    for dr in DIRECTION.keys():
        new_board = deepcopy(board)
        s_red, s_blue = simulator(new_board, red, blue, dr)
        dfs(cnt + 1, new_board, s_red, s_blue)


def simulator(board, red, blue, dr):
    """ 어느 구슬을 먼저 굴릴지 결정 """
    rr, rc = red
    br, bc = blue

    if dr == UP:
        if br < rr:  # blue가 더 위
            return simulator_first(board, red, blue, dr, BLUE)
        else:
            return simulator_first(board, red, blue, dr, RED)

    if dr == DOWN:
        if br > rr:
            return simulator_first(board, red, blue, dr, BLUE)
        else:
            return simulator_first(board, red, blue, dr, RED)

    if dr == LEFT:
        if bc < rc:
            return simulator_first(board, red, blue, dr, BLUE)
        else:
            return simulator_first(board, red, blue, dr, RED)

    if dr == RIGHT:
        if bc > rc:
            return simulator_first(board, red, blue, dr, BLUE)
        else:
            return simulator_first(board, red, blue, dr, RED)


def simulator_first(board, red, blue, dir, first):
    """ first에 따라 먼저 움직일 구슬 결정 """
    if first == RED:
        red = ball_simulator(board, red[0], red[1], dir, RED)
        blue = ball_simulator(board, blue[0], blue[1], dir, BLUE)
    else:  # BLUE 먼저
        blue = ball_simulator(board, blue[0], blue[1], dir, BLUE)
        red = ball_simulator(board, red[0], red[1], dir, RED)
    return red, blue


def ball_simulator(board, sr, sc, dir, color):
    """ 구슬 하나를 dir 방향으로 굴림 """
    board[sr][sc] = '.'
    dr, dc = DIRECTION[dir]
    r, c = sr, sc
    while True:
        nr, nc = r + dr, c + dc
        if board[nr][nc] == '.':  # 빈칸이면 계속 이동
            r, c = nr, nc
        elif board[nr][nc] == 'O':  # 구멍
            r, c = nr, nc
            break
        else:  # 벽 또는 다른 구슬
            break

    # 구멍이 아니라면 구슬을 현재 위치에 놓기
    if (r, c) != hole:
        board[r][c] = color
    return (r, c)


# DFS 탐색 시작
dfs(0, board, red, blue)

# 결과 출력
print(result if result != 11 else -1)
