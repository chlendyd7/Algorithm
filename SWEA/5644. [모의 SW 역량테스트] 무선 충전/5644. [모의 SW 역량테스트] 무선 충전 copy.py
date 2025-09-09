from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')
DIRECTION = {
    0: (0, 0),
    1: (0, 1),
    2: (1, 0),
    3: (-1, 0),
    4: (0, -1),
}

def solution():
    M, A = map(int, input().split())
    input1 = list(map(int, input().split()))
    input2 = list(map(int, input().split()))

    BC = defaultdict() #좌표, C(충전 범위), P(성능)
    BC_POWER = []
    for i in range(A):
        row, col, c, power = map(int, input().split())
        BC_POWER.append(power)
        BC[i] = (row, col, c, power)

    n_person1 = (0, 0)
    n_person2 = (9, 9)
    result = 0
    for i in range(M):
        tmp = []
        dx1, dy1 = DIRECTION[input1[i]]
        nx1, ny1 = n_person1[0] + dx1, n_person1[1] + dy1


        dx2, dy2 = DIRECTION[input2[i]]
        nx2, ny2 = n_person2[0] + dx2, n_person2[1] + dy2

        for idx, b_row, b_col, b_c, power in enumerate(BC):
            if abs(nx1 - b_row) + abs(ny2 - b_col) <= b_c:
               tmp.append((idx, power))
            if abs(nx2 - b_row) + abs(ny2 - b_col) <= b_c:
                tmp.append((idx, power))
        if tmp:
            tmp.sort(key=lambda x: x[0])
            result += tmp[0][1]
            if len(tmp) > 1:
                if tmp[0] == tmp[1]:
                    if tmp[0][1] // 2 < tmp[2][1]:
                        result += tmp[0][1]
                        continue
                else:
                    result += tmp[1][1]


    print(result)
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')