def solution():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    result = 0
    mid = N // 2
    for i in range(N):
        if i <= mid:
            start = mid - i
            end = mid + i
        else:
            start = i - mid
            end = (N - 1) - (i - mid)
        for j in range(start, end + 1):
            result += board[i][j]

    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
