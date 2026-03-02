import sys
import os

# 로컬에서 테스트할 때만 주석 해제


'''
    NxN 크기
    r,c r은 행 c는 열
    파이프는 회전 할 수 있음, 2칸을 차지한다
    →, ↘, ↓ 방향 밀면서 회전 가능
    꼭 빈칸 이여야 하는 경우 있음
    
    초기 파이프 (1,1) (1,2) 가로, (N,N으로 이동)
    집 크기 N <=16 완탐?
    벽은 1
'''
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
RIGHT = 1
DOWN = 2
DAGAK = 3
def check(r,c,shape):
    if shape == RIGHT:
        return c+1 < N and not board[r][c+1]
    elif shape == DOWN:
        return r+1 < N and not board[r+1][c]
    elif shape == DAGAK:
        if r + 1 < N and c + 1 < N:
            return not board[r+1][c] and not board[r][c+1] and not board[r+1][c+1]
    return False

def dfs(r, c, shape):
    global result
    if r == N-1 and c == N-1:
        result += 1
        return

    if shape == RIGHT or shape == DAGAK:
        if check(r,c, RIGHT):
            dfs(r, c+1, RIGHT)
    if shape == DOWN or shape == DAGAK:
        if check(r, c, DOWN):
            dfs(r+1, c, DOWN)
    if check(r,c,DAGAK):
        dfs(r+1, c+1, DAGAK)

dfs(0, 1, RIGHT)
print(result)


