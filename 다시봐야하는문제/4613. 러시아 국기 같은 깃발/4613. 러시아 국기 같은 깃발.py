from collections import defaultdict


def solution():
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    check = [[0,0,0] for _ in range(N)]
    for i in range(N):
        w, r, b = 0, 0, 0
        for j in range(M):
            color =  flag[i][j]
            if color == 'W':
                w += 1
            elif color == 'R':
                r += 1
            elif color == 'B':
                b += 1
        check[i][0] = w
        check[i][1] = b
        check[i][2] = r
    print(check)
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')