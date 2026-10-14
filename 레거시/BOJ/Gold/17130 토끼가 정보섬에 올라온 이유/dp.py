import sys

# 빠른 입력
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    
    # dp[r][c]: (r, c)에 도착했을 때의 최대 당근 수
    # 도달할 수 없는 곳은 -1로 초기화
    dp = [[-1] * M for _ in range(N)]
    
    rabbit_r, rabbit_c = -1, -1
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                rabbit_r, rabbit_c = r, c
                dp[r][c] = 0
                break

    # 열(c)을 기준으로 왼쪽에서 오른쪽으로 진행
    for c in range(rabbit_c + 1, M):
        for r in range(N):
            # 벽(' #')이면 건너뜀
            if board[r][c] == '#':
                continue
            
            # 이전 칸(c-1열)에서 올 수 있는 세 방향 체크
            prev_max = -1
            for dr in [-1, 0, 1]:
                pr = r + dr
                if 0 <= pr < N and dp[pr][c-1] != -1:
                    prev_max = max(prev_max, dp[pr][c-1])
            
            # 만약 이전 칸들 중 도달 가능한 곳이 있다면
            if prev_max != -1:
                # 현재 칸이 당근이면 +1, 아니면 그대로
                dp[r][c] = prev_max + (1 if board[r][c] == 'C' else 0)

    # 탈출구('O') 중 최댓값 찾기
    ans = -1
    for r in range(N):
        for c in range(rabbit_c + 1, M):
            if board[r][c] == 'O':
                ans = max(ans, dp[r][c])
                
    print(ans)

solve()