import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

'''
    cctv 벽 통과 x
    회전 시킬 수 있음 90도 방향
    NxM 크기 직사각형
    cctv는 cctv를 통과 할 수 있따
    사각지대를 최소화 하라
    cctv 방향 적절히 정해
'''

# 상(0), 우(1), 하(2), 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 종류별 감시 방향 (인덱스)
mode = [
    [],
    [[0], [1], [2], [3]],              # 1번: 한쪽
    [[0, 2], [1, 3]],                  # 2번: 직선 양쪽
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번: 직각
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번: 세 방향
    [[0, 1, 2, 3]]                     # 5번: 네 방향
]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctvs.append((i,j, board[i][j]))

def calculate(board):
    cnt = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                cnt += 1
    return cnt

def check(lst):
    # lst => r, c, d([0,2] or [1,3]...)
    new_board = [row[:] for row in board]
    for r, c, d_lst in lst:
        for d in d_lst:
            nr, nc = r, c
            while True:
                nr += dx[d]
                nc += dy[d]
                if 0 <= nr < N and 0 <= nc < M and new_board[nr][nc] != 6:
                    new_board[nr][nc] = '#'
                else:
                    break
    
    return calculate(new_board)

mn = float('inf')
def dfs(depth, lst):
    global mn
    # 모든 cctv를 찾았으면 실행
    if depth == len(cctvs):
        mn = min(mn, check(lst))
        return

    r, c, tv = cctvs[depth]
    for d in mode[tv]: # d => [0,2], [1,3]
        lst.append((r,c,d))
        dfs(depth+1, lst)
        lst.pop()

dfs(0, [])
print(mn)
