from copy import deepcopy

def solution():
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    # K == 1 은 무조건 통과 (약품 0회)
    if K == 1:
        return 0

    visited = [0] * D

    def check_board(b):
        # 각 열에 대해 세로로 연속 K 확인
        for w in range(W):
            run = 1
            ok = False
            for d in range(1, D):
                if b[d][w] == b[d-1][w]:
                    run += 1
                else:
                    run = 1
                if run >= K:
                    ok = True
                    break
            if not ok:
                return False
        return True

    # 현재 보드가 이미 통과면 0
    if check_board(board):
        return 0

    def dfs(limit, picked, start, b):
        # limit개를 다 골랐으면 성능 검사
        if picked == limit:
            return check_board(b)

        # 가지치기: 남은 행 수 < 필요한 선택 수면 실패 가지치기 부분 잘 보기
        if D - start < limit - picked:
            return False

        for d in range(start, D):
            if visited[d]:
                continue
            visited[d] = 1
            row_backup = b[d][:]

            # 약품 A
            b[d] = [0] * W
            if dfs(limit, picked + 1, d + 1, b):
                return True

            # 약품 B
            b[d] = [1] * W
            if dfs(limit, picked + 1, d + 1, b):
                return True

            # 원복
            b[d] = row_backup
            visited[d] = 0
        return False

    # 최소 투입 횟수부터 증가시키며 탐색
    for length in range(1, D + 1):
        tmp_board = deepcopy(board)
        if dfs(length, 0, 0, tmp_board):
            return length

T = int(input())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')
