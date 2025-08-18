# https://www.acmicpc.net/problem/1600
from collections import deque
import sys
input = sys.stdin.readline

# 말의 이동 (나이트 이동)
horse = [
    (2, 1), (1, 2), (2, -1), (1, -2),
    (-1, 2), (-2, 1), (-1, -2), (-2, -1)
]

# 일반 이동 (상하좌우)
direction = [
    (1, 0), (0, 1), (-1, 0), (0, -1)
]

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

def solution():
    visited = [[[0] * (K+1) for _ in range(W)]  for _ in range(H)]    
    q = deque([(0, 0, 0)])
    cnt = 0
    while q:
        for _ in range(len(q)):
            r, c, wall = q.popleft()
            if r == H-1 and c == W-1:
                return cnt
            
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                if 0 <= nr < H and 0 <= nc < W and not board[nr][nc] and not visited[nr][nc][wall]:
                    visited[nr][nc][wall] = 1
                    q.append((nr, nc, wall))

            if wall < K:
                for dx, dy in horse:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < H and 0 <= nc < W and not board[nr][nc] and not visited[nr][nc][wall + 1]:
                        visited[nr][nc][wall+1] = 1
                        q.append((nr, nc, wall + 1))
        cnt += 1

    return -1

print(solution())
