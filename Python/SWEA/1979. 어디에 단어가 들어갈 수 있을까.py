def solution(board, K):
    count = 0
    for line in board:
        extended_line = [0] + line + [0]
        current_length = 0
        for cell in extended_line:
            if cell == 1:
                current_length += 1
            else:
                if current_length == K:
                    count += 1
                current_length = 0

    return count

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    total = solution(board, K)
    transport = zip(*board)
    vertical_board = [list(tp) for tp in transport]
    total += solution(vertical_board, K)

    print(f"#{t} {total}")
