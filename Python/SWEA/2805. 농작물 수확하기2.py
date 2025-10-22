from collections import defaultdict

def solution():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    cnt = 0
    for i in range(N):
        if i <= mid:
           for j in range(mid - i, mid + i + 1):
               cnt += board[i][j] 
        else:
            for j in range(i - mid, (N - 1) - (i - mid) + 1):
                cnt += board[i][j]

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
