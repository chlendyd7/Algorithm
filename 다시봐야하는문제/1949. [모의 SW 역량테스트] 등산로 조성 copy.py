# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
'''
최대한 긴 등산로를 만들 계획
N 8
공사 가능 깊이 5
지형 높이 20
가장 높은 봉우리 5

백트래킹 완탐

N*N board
등산로는 가장 높은 봉우리에서 시작해야함
연결되야함
딱 한 곳을 정해서 최대 K 깊이 만큼 지형을 깎는 공사를 할 수 있다.

모든 곳을 탐색하는게 아닌

bfs가 아닌 dfs로 풀어라고함
'''
from collections import deque
from copy import deepcopy
DIRECTION = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def solution():
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    mx_len = 0

    mx = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > mx:
                mx = mountain[i][j]
                points = [(i,j)]

            elif mountain[i][j] == mx:
                points.append((i,j))

    def dfs(r,c, length, visited, board):
        nonlocal mx_len
        mx_len = max(mx_len, length)

        for dr, dc in DIRECTION:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] < board[r][c]:
                    visited[nr][nc] = 1
                    dfs(nr, nc, length + 1, visited, board)
                    visited[nr][nc] = 0

    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                mountain[i][j] -= k
                for sr, sc in points:
                    visited = [[0] * N for _ in range(N)]
                    visited[sr][sc] = 1
                    dfs(sr, sc, 1, visited, mountain)
                    visited[sr][sc] = 0
                mountain[i][j] += k

    return mx_len

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')