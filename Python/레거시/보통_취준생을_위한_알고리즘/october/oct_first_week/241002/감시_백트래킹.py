from collections import deque
import sys


input = sys.stdin.readline

N, M = map(int,input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def check(row, col):
    return 0<= row < N and 0<= col < M

def init():
    obj = deque()
    answer = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))
            if space[i][j] == 0:
                answer += 1
    return obj, answer

cctv, answer = init()

