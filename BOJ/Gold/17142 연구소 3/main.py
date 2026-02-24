'''
    M개를 활성화 상태로 변경하려고 함
    0은 빈칸 1은 벽 2는 바이러스
'''
from collections import deque
import itertools

def bfs(selected_virus, total_empty, min_time):
    q = selected_virus
    visited = [[0] * N for _ in range(N)]
    for r, c in selected_virus:
        visited[r][c] = 1

    cnt = 0
    time = 0
    while True:
        if time >= min_time:
            return float('inf')

        next_q = []
        for r, c in q:
            
            for rr, cc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r + rr, c + cc
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc] and board[nr][nc] != 1:
                        visited[nr][nc] = 1
                        next_q.append((nr, nc))
                        if board[nr][nc] == 0:
                            cnt += 1

        # print(time)
        time += 1
        q = next_q

        if cnt == total_empty:
            return time

N, M = map(int, input().split())
virus = set()
complete = 0
board = []
for i in range(N):
    inputs = list(map(int, input().split()))
    board.append(inputs)
    for j in range(N):
        if inputs[j] == 2:
            virus.add((i,j))
        elif inputs[j] == 0:
            complete += 1

min_value = float('inf')
for select_virus in itertools.combinations(virus, M):
    min_value = min(min_value, bfs(select_virus, complete, min_value))
print(min_value)
