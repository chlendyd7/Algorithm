def solution(board, K):
    cnt = 0
    for row in board:
        row = [0] + row + [0]
        tmp = 0
        for r in row:
            if r == 1:
                tmp += 1
            else:
                if tmp == K:
                    cnt += 1
                tmp = 0
    return cnt

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = solution(board, K)
    reverse_board = zip(*board)
    reversed_board_lst = [list(row) for row in reverse_board]
    result += solution(reversed_board_lst, K)
    print(f'#{t} {result}')