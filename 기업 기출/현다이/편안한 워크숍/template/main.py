import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

'''
입사동기들의 의견을 만족하는 등산로 중 인접한 높이의 차들 간의 최댓값이 최소가 되는 등산로가 가장 편안한 등산로입니다.

등산로는 어느 칸에서 시작해도 상관 없습니다.
등산로는 시작칸으로부터 상하좌우로 인접한 칸으로만 이동하는 것을 원칙으로 하며, 이동할 때마다 높이가 높아져야 합니다.
등산로의 길이는 K 이상이어야 합니다. 등산로의 길이는 해당 등산로로 갈 때 지나가는 칸의 수를 의미합니다.

2 <= N <= 100, 2 <= K <= 100

'''
N , K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cells = []

def check(diff_limit):
    dp =[[1] * N for _ in range(N)]
    max_len = 0
    for h, r, c in cells:
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] < h and h - board[nr][nc] <= diff_limit:
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
        max_len = max(max_len, dp[r][c])
        if max_len >= K:
            return True
    return False

low = 0
high = 10 ** 8
answer = -1
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

    print(answer)
