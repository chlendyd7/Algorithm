from collections import deque
import sys
input = sys.stdin.readline
'''
    가장 적은 개수의 칸을 지나는 경로
    1,1 => N,M 으로 가야함

    배운점: bfs 간선의 가중치가 다 같다면 도착하는게 가장 빠른거임

    ## 아이디어
    - N,M 으로 가까워지는거만 뚫기
    - 3. 불필요한 상태 pruning
        이미 더 적은 벽을 부수고 같은 위치에 도달한 경우가 있다면 스킵
        visited[x][y][k]가 True이면서 현재보다 적은 k로 방문했다면 continue
'''
direction = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

greedy_d = [
    (1,0),
    (0,1)
]

# N x M 행렬 k개 벽을 부술 수 있음
N, M, K = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
result = 1e9

def calculate():
    q = deque([(0,0,0)])
    visited[0][0][0] = 1
    while q:
        size_q = len(q)
        for _ in range(size_q):
            r, c, wall = q.popleft()
            if r == N-1 and c == M-1:
                return visited[r][c][wall]

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                flag = False
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][wall]:
                    for i in range(wall):
                        if visited[nr][nc][i]:
                            flag = True
                            break
                    if maze[nr][nc] == 0:
                        visited[nr][nc][wall] = visited[r][c][wall] + 1
                        q.append((nr, nc, wall))
                    elif maze[nr][nc] == 1 and wall < K:
                        visited[nr][nc][wall+1] = visited[r][c][wall] + 1
                        q.append((nr, nc, wall + 1))
                if flag:
                    continue

    return -1

print(calculate())