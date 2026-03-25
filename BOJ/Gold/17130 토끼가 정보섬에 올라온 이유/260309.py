import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
rabbit = None
for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            rabbit = (r,c)

for c in range(M):
    if dp[0][c] == 'C':
        dp[0][c] = 1

for c in range(1, M):
    for r in range(N):
        for nr, nc in ((0,1), (1,1), (-1,1)):
            pr = r - nr
            pc = r - nc
            if 0 <= pr < N and 0 <= pc < M: 
                if board[r][c] == 'C':
                    dp[r][c] = max(dp[r][c], dp[pr][pc] + 1)
                elif board[r][c] == '#':
                    continue
                else:
                    dp[r][c] = max(dp[r][c], dp[pr][pc])

mx = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'O':
            mx = max(mx, dp[r][c])
print(mx)