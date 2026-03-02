'''
    N <= 250 행렬 양수
    K개의 질문 BxB 부분행렬의 최대값 최소값
    각 질문 부분 행렬의 가장 왼쪽 위 위치

    N,B,K
    i,j 가장 왼쪽, 행 열 번호
'''
from collections import deque


N, B, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_row = [[0] * (N-B+1) for _ in range(N)]
min_row = [[251] * (N-B+1) for _ in range(N)]

for r in range(N):
    for c in range(N-B+1):
        target = board[r][c:c+B]
        max_row[r][c] = max(target)
        min_row[r][c] = min(target)

# 세로도 전처리
final_max = [[0] * (N-B+1) for _ in range(N)]
final_min = [[251] * (N-B+1) for _ in range(N)]

for c in range(N-B+1):
    for r in range(N-B+1):
        target_max = [max_row[nr][c] for nr in range(r, r+B)]
        target_min = [min_row[nr][c] for nr in range(r, r+B)]
        final_max[r][c] = max(target_max)
        final_min[r][c] = min(target_min)


for _ in range(K):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    print(final_max[i][j] - final_min[i][j])


def get_sliding_max(arr, B):
    res = []
    dq = deque()
    for i in range(len(arr)):
        if dq and dq[0] <= i-B:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= B - 1:
            res.append(arr[dq[0]])
    return res
