import sys
from collections import deque

# 빠른 입력을 위해 설정
input = sys.stdin.readline

def get_window_vals(arr, b, find_max=True):
    """
    1차원 배열에서 크기가 b인 슬라이딩 윈도우의 최대/최소값을 구하는 함수
    """
    results = []
    dq = deque()
    
    for i in range(len(arr)):
        # 1. 새로 들어온 값(arr[i])보다 쓸모없는 값들은 덱(deque)에서 제거
        if find_max:
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
        else:
            while dq and arr[dq[-1]] >= arr[i]:
                dq.pop()
        
        dq.append(i)
        # 2. 윈도우 범위를 벗어난 인덱스 제거 (가장 왼쪽 값)
        if dq[0] <= i - b:
            dq.popleft()
            
        # 3. 윈도우 크기(b)가 충족되었을 때부터 결과값 저장
        if i >= b - 1:
            results.append(arr[dq[0]])
            
    return results

def solve():
    # 데이터 입력 및 기본 설정
    line1 = input().split()
    if not line1: return
    N, B, K = map(int, line1)
    
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    # --- 1단계: 모든 행(Row)에 대해 가로 방향 윈도우 최대/최소 구하기 ---
    row_max_matrix = []
    row_min_matrix = []
    
    for r in range(N):
        max_row = get_window_vals(board[r], B, find_max=True)
        min_row = get_window_vals(board[r], B, find_max=False)
        row_max_matrix.append(max_row)
        row_min_matrix.append(min_row)

    # --- 2단계: 위 결과물을 세로 방향으로 다시 윈도우 최대/최소 구하기 ---
    # 가로로 압축된 배열의 열 개수 = N - B + 1
    num_cols = N - B + 1
    
    # 최종 결과를 담을 공간 (각 좌표를 시작점으로 하는 BxB의 결과)
    final_max = []
    final_min = []

    for c in range(num_cols):
        # 각 열(Column) 데이터를 추출
        current_col_max = []
        current_col_min = []
        for r in range(N):
            current_col_max.append(row_max_matrix[r][c])
            current_col_min.append(row_min_matrix[r][c])
        
        # 추출한 열 데이터에 대해 슬라이딩 윈도우 적용
        final_max.append(get_window_vals(current_col_max, B, find_max=True))
        final_min.append(get_window_vals(current_col_min, B, find_max=False))

    # --- 3단계: 쿼리 처리 ---
    for _ in range(K):
        r, c = map(int, input().split())
        # 입력은 1-based이므로 0-based 인덱스로 변환 (r-1, c-1)
        # 2단계에서 열(c) 기준으로 결과를 쌓았으므로 인덱스 접근 시 [c-1][r-1] 주의
        res_max = final_max[c-1][r-1]
        res_min = final_min[c-1][r-1]
        print(res_max - res_min)

solve()

