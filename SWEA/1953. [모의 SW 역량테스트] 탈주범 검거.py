# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
'''
탈주범은 시간당 1의 거리를 움직일 수 있다.
탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.
bfs로 나아가면서 다음 위치 터널 구조물이 있을 때 서로 연결이 가능한 구조인가
'''
from collections import deque

pip = {
    1:[(1,0), (0,1), (-1, 0), (0, -1)],
    2: [(1,0), (-1,0)],
    3: [(0,1), (0,-1)],
    4: [(-1,0), (0,1)],
    5: [(1,0), (0,1)],
    6: [(1, 0), (0,-1)],
    7: [(-1,0), (0,-1)],
}

opposite = {
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
    (0, -1): (0, 1),
    (0, 1): (0, -1),
}


def solution():
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    time = 1
    q = deque([(time, R, C)])
    visited[R][C] = 1

    while q:
        n_time, r, c = q.popleft()

        if n_time >= L:
            continue

        for dr, dc in pip[board[r][c]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M \
                and not visited[nr][nc] and board[nr][nc]:
                if opposite[(dr,dc)] in pip[board[nr][nc]]:
                    visited[nr][nc] = 1
                    q.append((n_time + 1, nr, nc))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
