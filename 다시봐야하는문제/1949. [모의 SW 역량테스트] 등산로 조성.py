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
DIRECTION = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def solution():
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > mx:
                mx = mountain[i][j]
                points = [(i,j)]
            
            elif mountain[i][j] == mx:
                points.append((i,j))
    print(mx, points)

    def find_max_line(board):
        mx_len = 0
        visited = [[0] * N for _ in range(N)]
        for i,j in points:
            q = deque([(i,j)])
            visited[i][j] = 1
            check_len = 0
            while q:
                size_q = len(q)
                check_len += 1
                for _ in range(size_q):
                    r, c = q.popleft()
                    for dr, dc in DIRECTION:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and board[r][c] > board[nr][nc] and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
            mx_len = max(mx_len, check_len)
        return mx_len

    def dfs(i,j, start):
        mx_len = 0
        origin = mountain[i][j]
        for i in range(start + 1, K+1):
            mountain[i][j] -= i
            mx_len = max(mx_len, find_max_line(mountain))
            mountain[i][j] = origin
        return mx_len

    for i in range(N):
        for j in range(N):
            check = False
            if (i, j) in points:
                points.remove((i,j))
                check = True
            mx = max(mx, dfs(i, j, 0))
            if check:
                points.append((i,j))

    return mx

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')