direction = [
    (0,1),
    (1,0),
    (1,1),
    (1,-1),
]
def solution():
    N = int(input())
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for di, dj in direction:
                    ni, nj = i, j
                    print(ni, nj)
                    cnt = 1
                    for _ in range(4):
                        ni, nj = ni + di, nj + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if board[ni][nj] == 'o':
                                cnt += 1
                            else:
                                break
                    if cnt == 5:
                        return True
    return False


T = int(input())
for t in range(1, T+1):
    check = solution()
    # result = "Yes" if check else 'NO'
    # if check:
    #     result
    print(f'#{t}', 'YES' if check else 'NO')
