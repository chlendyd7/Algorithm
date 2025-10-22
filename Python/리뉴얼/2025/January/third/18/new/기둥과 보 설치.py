# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
from collections import deque


def solution(n, build_frame):
    columns = [[0] * n for _ in range(n)]
    rows = [[0] * n for _ in range(n)]
    
    for build in build_frame:
        x, y, a, b = build
        if b == 1: # create
            if a == 0: # 기둥
                if y == 0:
                    columns[x][y] = 1
                else:
                    if columns[x][y-1] or rows[x-1][y]:
                        columns[x][y] = 1
            else:
                if columns[x][y-1] or columns[x+1][y-1]:
                    rows[x][y] = 1

        else:
            q = deque([x,y,a])
            while q:
                if a == 0:
                    columns[x][y] = 0
                    if columns[x][y+1]:
                        q.append([x,y+1,0])
                    elif rows[x][y-1]:
                        q.append([x,y-1, 0])
                else:
                    rows[x][y] = 0
                    if columns[x-1][y-1]:
                        q.append([x])

    answer = [[]]
    return answer