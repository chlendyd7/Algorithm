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
    # person1 = []
    # person2 = []
    # for i in range(0, M, 2):
    #     person1.append((input1[i], input1[i+1]))
    #     person2.append((input2[i], input2[i+1]))

    BC = defaultdict(list) #좌표, C(충전 범위), P(성능)
    BC_POWER = []
    for i in range(A):
        #좌표, C(충전 범위), P(성능)
        row, col, c, power = map(int, input().split())
        BC_POWER.append(power)
        for x in range(row - c, row + c + 1):
            for y in range(col - c, col + c + 1):
                if abs(x - row) + abs(y - col) <= c:
                    BC[i].append((x, y))

    n_person1 = (0, 0)
    n_person2 = (9, 9)
    result = 0
    for i in range(M):
        dx1, dy1 = DIRECTION[input1[i]]
        nx1, ny1 = n_person1[0] + dx1, n_person1[1] + dy1
        

        dx2, dy2 = DIRECTION[input2[i]]
        nx2, ny2 = n_person2[0] + dx2, n_person2[1] + dy2

        for 
        if (nx1, ny1) in 


        for bc in BC.keys():
            if ()


    print(person1)
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')