'''
N * N 표의 크기
*면 지뢰 . 면 지뢰 없음
지뢰 있는 칸의 숫자들을 표시되려면 최소 몇 번의 클릭을 해야하는지 구하라

숫자가 0 이면 그 방향 8개의 칸도 자동으로 숫자를 표시

bfs로 접근했는데 그 nx, ny를 q에 추가해 주어야 하는지 않는지 체크하는 부분에서 막힘
'''
from collections import deque
direction = [
    (1,0),
    (1,1),
    (1,-1),
    (0,1),
    (0,-1),
    (-1,0),
    (-1,1),
    (-1,-1)
]

def solution():
    N = int(input())
    board = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    mine_count = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                mine_count[i][j] = -1
                continue
            count = 0
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '*':
                    count += 1
            mine_count[i][j] = count
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            cx, cy = q.popleft()
            if mine_count[cx][cy] == 0:
                for dx, dy in direction:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and mine_count[nx][ny] != -1:
                            visited[nx][ny] = True
                            q.append((nx, ny))

    clicks = 0
    for i in range(N):
        for j in range(N):
            if mine_count[i][j] == 0 and not visited[i][j]:
                bfs(i, j)
                clicks += 1

    for i in range(N):
        for j in range(N):
            if mine_count[i][j] != -1 and not visited[i][j]:
                clicks += 1

    return clicks


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
