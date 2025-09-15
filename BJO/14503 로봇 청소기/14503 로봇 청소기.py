'''
    N x M
    동서남북 r,c

    주변4칸 중 청소되지 않은 빈칸이 없는 경우 바라보는 방향을 유지하며 후진
    청소되지 않는 빈칸이 있는 경우 반 시계 방향으로 회전
    청소하는 칸의 개수를 출력
'''

NORHT = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTION = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

N, M = map(int, input().split())
r,c,d = map(int, input().split())
