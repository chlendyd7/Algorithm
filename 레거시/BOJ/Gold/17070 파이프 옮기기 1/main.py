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


import sys
from functools import lru_cache

# 재귀 깊이 제한 해제 (파이썬 기본은 1000이라 N이 커지면 위험함)
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

RIGHT, DOWN, DAGAK = 0, 1, 2

def check(r, c, shape):
    if shape == RIGHT:
        return c + 1 < N and board[r][c + 1] == 0
    elif shape == DOWN:
        return r + 1 < N and board[r + 1][c] == 0
    elif shape == DAGAK:
        if r + 1 < N and c + 1 < N:
            return board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0
    return False

@lru_cache(None)
def dfs(r, c, shape):
    # 목적지 도달 시 경우의 수 1 반환
    if r == N - 1 and c == N - 1:
        return 1
    
    cnt = 0
    # 1. 가로 이동
    if shape == RIGHT or shape == DAGAK:
        if check(r, c, RIGHT):
            cnt += dfs(r, c + 1, RIGHT)
            
    # 2. 세로 이동
    if shape == DOWN or shape == DAGAK:
        if check(r, c, DOWN):
            cnt += dfs(r + 1, c, DOWN)
            
    # 3. 대각선 이동
    if check(r, c, DAGAK):
        cnt += dfs(r + 1, c + 1, DAGAK)
        
    return cnt

# 시작: (0, 1) 위치에 가로(RIGHT) 상태
print(dfs(0, 1, RIGHT))