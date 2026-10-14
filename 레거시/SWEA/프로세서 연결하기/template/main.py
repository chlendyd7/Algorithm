import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

direction = [(1,0), (0,1), (-1,0), (0,-1)]
def solve():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    hubo = []
    for r in range(1, N-1):
        for c in range(1, N-1):
            if board[r][c] == 1:
                hubo.append((r,c))
    total_cores = len(hubo)
    min_length = float('inf')
    max_cores = 0

    def dfs(idx, connect_count, current_length):
        nonlocal max_cores, min_length
        
        if (total_cores - idx) + connect_count < max_cores:
            return
        
        if idx == total_cores:
            if connect_count > max_cores:
                max_cores = connect_count
                min_length = current_length
            elif connect_count == max_cores:
                min_length = min(min_length, current_length)
            return
        
        r, c = hubo[idx]
        for dr, dc in direction:
            path = []
            nr, nc = r + dr, c + dc
            can_go = True
            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 0:
                    break
                path.append((nr, nc))
                nr += dr
                nc += dc
            
            if can_go:
                for pr, pc in path: board[pr][pc] = 2
                dfs(idx +1, connect_count+1, current_length + len(path))
                for pr, pc in path: board[pr][pc] = 0
        dfs(idx+1, connect_count, current_length)
        
    dfs(0,0, 0)
    return min_length
T = int(input())
for t in range(1, T+1):
    print(solve())
