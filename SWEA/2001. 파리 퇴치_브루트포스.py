def max_flies_killed(board, N, M):
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N -M + 1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += board[i + x][j + y]
            max_kill = max(max_kill, total)
    return max_kill

T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {max_flies_killed(board, N, M)}')
