from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

# 3차원 배열로 방문 체크 (시간/메모리 효율)
# visited[r][c][능력 사용 횟수]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]

# 상하좌우, 말 이동 좌표
direction = [(0,1), (1,0), (-1,0), (0,-1)]
horse = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

def solution():
    # 예외 처리: 시작점과 도착점이 같은 경우
    if w == 1 and h == 1:
        return 0

    q = deque([(0, 0, 0)]) # r, c, k_used
    visited[0][0][0] = 0
    
    while q:
        r, c, used = q.popleft()
        
        # 현재 이동 횟수
        dist = visited[r][c][used]
        
        # 1. 일반 이동
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0:
                if visited[nr][nc][used] == -1:
                    if nr == h-1 and nc == w-1: return dist + 1 # 조기 종료
                    visited[nr][nc][used] = dist + 1
                    q.append((nr, nc, used))
        
        # 2. 말 이동
        if used < k:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0:
                    if visited[nr][nc][used + 1] == -1:
                        if nr == h-1 and nc == w-1: return dist + 1 # 조기 종료
                        visited[nr][nc][used + 1] = dist + 1
                        q.append((nr, nc, used + 1))
    
    return -1

print(solution())
