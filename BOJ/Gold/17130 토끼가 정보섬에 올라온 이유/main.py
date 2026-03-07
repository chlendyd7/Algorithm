from collections import deque
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

'''
    N행 M열의 격자
    토끼 방향 →, ↘, ↗
    최대한 많은 당근을 줍고 싶음
    정문x 쪽문으로, 쪽문 도착해도 더 움직여도 됨
    얼마나 많은 당근 (최대 당근)
    '.'빈공간, '#'은벽, 'R'은 토끼, 'C'는 당근, 'O'는 정보섬 쪽문
'''

N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
rabbit = None
direct = [(0,1), (1,1), (-1,1)]
rabbit_r, rabbit_c = -1, -1
for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            rabbit_r, rabbit_c = r, c
            dp[r][c] = 0
            break

for c in range(rabbit_c + 1, M):
    for r in range(N):
        if board[r][c] == '#':
            continue
    
        prev_max = -1
        for dr in [-1,0,1]:
            pr = r + dr
            if 0 <= pr < N and dp[pr][c-1] != -1:
                prev_max = max(prev_max, dp[pr][c-1])
                

dp = [[0] * M for _ in range(N)]
q = deque([[0, *rabbit]])
cnt = -1
while q:
    carrot, r, c = q.popleft()
    for dr, dc in direct:
        nr, nc = r + dr, c + dc
        if 0<= nr < N and 0<= nc < M:
            if board[nr][nc] == 'C':
                q.append([carrot+1, nr, nc])
            elif board[nr][nc] == 'O':
                cnt = max(cnt, carrot)
                q.append([carrot, nr, nc])
            elif board[nr][nc] == '.':
                q.append([carrot, nr, nc])

print(cnt)