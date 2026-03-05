import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

def check():
    for start in range(1, N+1):
        curr = start
        for r in range(1, H+1):
            if board[r][curr] == 1:
                curr += 1
            elif board[r][curr-1] == 1:
                curr -= 1
        if curr != start:
            return False
    return True

def dfs(cnt, r, c):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = cnt
        return
    if cnt == 3:
        return

    for i in range(r, H+1):
        if i == r:
            k = c
        else:
            k = 1
        for j in range(k, N):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0
ans = 4
dfs(0,1,1)
print(ans)