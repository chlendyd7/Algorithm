import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def solve():
    N = int(input())
    board = [[0] * 101 for _ in range(101)]
    
    for _ in range(N):
        x, y, d, g = map(int, input().split())
    
        dirs = [d]
        for _ in range(g):
            for i in range(len(dirs)-1, -1, -1):
                dirs.append((dirs[i]+1) % 4)

        board[x][y] = 1
        for d in dirs:
            x += dx[d]
            y += dy[d]
            if 0 <= x <= 100 and 0 <= y <= 100:
                board[x][y] = 1

    ans = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                ans += 1
    print(ans)
solve()
