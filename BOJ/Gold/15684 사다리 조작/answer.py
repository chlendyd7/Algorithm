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

def dfs(cnt, r, c, target):
    global found
    if found: return
    
    if cnt == target:
        if check():
            found = True
        return

    for i in range(r, H + 1):
        # 행이 바뀌면 1열부터, 같은 행이면 이전 c부터
        start_c = c if i == r else 1
        for j in range(start_c, N): # N-1번 열까지만 가로선을 놓을 수 있음
            # 1. 현재 자리에 가로선이 없고
            # 2. 왼쪽(j-1)에 가로선이 없고
            # 3. 오른쪽(j+1)에 가로선이 없는지 확인
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                dfs(cnt + 1, i, j + 2, target) # 연속 설치 불가니 j+2
                board[i][j] = 0
                if found: return

found = False
for limit in range(4):
    dfs(0,1,1,limit)
    if found:
        print(limit)
        exit()

print(-1)