'''
- N^2개의 방이 N x N
- 숫자 범위: 1이상 N^2이하
- 상하좌우 이동
- 이동하려는 방이 현재 방에 적힌 숫자보다 정확히 1 더 커야함
- 처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하라
'''
from collections import deque

direction = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0)
]
def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cache = [[0]*N for _ in range(N)]

    def dfs(x, y):
        if cache[x][y] != 0:
            return cache[x][y]

        max_len = 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == board[x][y] + 1:
                max_len = max(max_len, 1 + dfs(nx, ny))
        cache[x][y] = max_len
        return max_len

    max_move = 0
    min_start = float('inf')

    for i in range(N):
        for j in range(N):
            length = dfs(i, j)
            if length > max_move:
                max_move = length
                min_start = board[i][j]
            elif length == max_move:
                min_start = min(min_start, board[i][j])
    return f'{min_start} {max_move}'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
