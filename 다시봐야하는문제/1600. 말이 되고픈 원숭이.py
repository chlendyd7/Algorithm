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
    # 3차원 방문 체크: visited[r][c][k] = (r,c)를 k번의 말 이동으로 방문했는지
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    
    # 큐: (행, 열, 사용한_말_이동_횟수, 총_이동_횟수)
    q = deque([(0, 0, 0, 0)])
    visited[0][0][0] = True
    
    while q:
        r, c, count_k, distance = q.popleft()
        
        # 도착점 도달
        if r == H - 1 and c == W - 1:
            return distance
        
        # 일반 이동 (상하좌우)
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W:
                if not board[nr][nc] and not visited[nr][nc][count_k]:
                    visited[nr][nc][count_k] = True
                    q.append((nr, nc, count_k, distance + 1))
        
        # 말 이동 (나이트 이동) - K번 제한
        if count_k < K:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if not board[nr][nc] and not visited[nr][nc][count_k + 1]:
                        visited[nr][nc][count_k + 1] = True
                        q.append((nr, nc, count_k + 1, distance + 1))
    
    return -1

print(solution())
