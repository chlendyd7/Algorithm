def solution():
    N, M = map(int, input().split())
    lst = [list(map(int, input())) for _ in range(N)]
    check = False

    # find start_idx
    for i in range(N):
        if check:
            break
        for j in range(M):
            if lst[i][j] == 1:
                start_idx = (i, j)
                check = True
                break

    password = []
    print(start_idx)
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')