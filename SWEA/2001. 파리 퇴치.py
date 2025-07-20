def max_flies_killed(board, N, M):
    # 누적합 배열 초기화 (1-based indexing을 위해 N+1 x N+1)
    prefix = [[0] * (N + 1) for _ in range(N + 1)]

    # 누적합 배열 채우기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = (board[i-1][j-1]
                            + prefix[i-1][j]
                            + prefix[i][j-1]
                            - prefix[i-1][j-1])

    # M x M 구간 중 최댓값 찾기
    max_kill = 0
    for i in range(M, N + 1):
        for j in range(M, N + 1):
            total = (prefix[i][j]
                    - prefix[i-M][j]
                    - prefix[i][j-M]
                    + prefix[i-M][j-M]
                    )
            max_kill = max(max_kill, total)

    return max_kill

T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {max_flies_killed(board, N, M)}')
