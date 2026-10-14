'''
    끝 점을 기준으로 시계 방향 90도 회전
    시계 방향으로 90도 회전?

    K-1 세대 드래곤 커브를 끝 점을 기준으로 90도 회전, 끝 점에 붙임
    정사각형의 개수를 구하라
    크기가 1x1인 정사각형

    x, y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
    격자 밖으로 나가지 않는다

    방향
    0: x 오른쪽
    1: y 감소 윗쪽
    2: x좌표 감수 왼쪽
    3: y좌표 증가 아래

    3
    3 3 0 1
    4 2 1 3
    4 2 2 1
'''
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


def simul(r, c, diect):
    pass
def solve():
    board = [[0] * 100 for _ in range(100)]
    N = int(input())
    dragons = [list(map(int, input().split())) for _ in range(N)]
    directoin = [(0,1), (-1,0), (0,-1), (1,0)]
    
    for c, r, direct, g in dragons:
        # 그 전 값 가지고 있기
        # 근데 형태는 다 같음
        prev = [(r,c)]
        for _ in range(g):
            new_prev = []
            for r,c in prev:
                board[]


while True:
    try:
        pass
    except EOFError:
        break
