import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

'''
    N,M 직사각형 형태 나무 재료 부위마다 그 강도가 조금씩 다름
    부메랑은 항상 ㄱ 모양으로
    부메라 중심은 강도의 영향을 2배
    만들 수 있는 부메랑들의 강도 합의 최대값을 출력
'''
N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
max_value = 0
shapes = [
    [(0, -1), (0, 0), (1, 0)],  # ┓ 모양 (중심이 0,0)
    [(-1, 0), (0, 0), (0, -1)], # ┛ 모양
    [(-1, 0), (0, 0), (0, 1)],  # ┗ 모양
    [(0, 1), (0, 0), (1, 0)]    # ┏ 모양
]
def dfs(idx, current_sum):
    global ans
    if idx == N * M:
        ans = max(ans, current_sum)
        return
    
    r = idx // M
    c = idx % M

    if not check[r][c]:
        for shape in shapes:
            possible = True
            temp_sum = 0

            for i, (dr, dc) in enumerate(shape):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < M) or check[nr][nc]:
                    possible = False
                    break
                temp_sum += board[nr][nc] * (2 if i == 1 else 1)

            if possible:
                for dr, dc in shape:
                    check[r+dr][c+dc] = True
                dfs(idx+1, current_sum+temp_sum)
                for dr, dc in shape:
                    check[r+dr][c+dc] = False
    dfs(idx + 1, current_sum)
