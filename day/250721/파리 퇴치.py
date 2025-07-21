def solution(n, m, board):
    prefix = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix[i][j] = (
                board[i-1][j-1]
                + prefix[i-1][j]
                + prefix[i][j-1]
                - prefix[i-1][j-1]
            )

    max_result = 0
    for i in range(m, n+1):
        for j in range(m, n+1):
            result = (
                prefix[i][j]
                - prefix[i-m][j]
                - prefix[i][j-m]
                + prefix[i-m][j-m]      
                )
            max_result = max(max_result, result)

    return max_result


T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t} {solution(n, m, board)}')
