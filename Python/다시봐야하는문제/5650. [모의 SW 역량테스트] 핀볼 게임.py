'''
NxN 4가지 형태 삼각형 블록
웜홀과 블랙홀
상 하 좌 우
블록과 웜홀, 블랙홀을 만나면 정지 아니면 계속 직진
경사면은 직각으로 방향 꺾이고 아니면 반대 방향으로 돌아옴
벽에 만나도 반대 방향으로 옴

핀볼이 출발 위치로 돌아오거나
블랙홀데 빠질 때 끝남

벽이나 블록에 부딪힌 횟수가 점수
출발 위치와 진행 방향을 임의로 선정 가능

**게임에서 얻을 수 있는 점수의 최대 값**, 블록 웜홀 블랙홀에서는 출발 X
1,2,3,4,5 블록
6~10 웜홀
-1 블랙홀

벽(0, N)

블록 아이디어: 해당 key 안에 있으면 다음 방향으로 이동시키는데 아니면 그냥 reverse
'''
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

opposite = {
    RIGHT:LEFT,
    LEFT:RIGHT,
    UP:DOWN,
    DOWN:UP
}

blocks = {
    1: {DOWN: RIGHT, LEFT: UP},
    2: {UP: RIGHT, LEFT: DOWN}, 
    3: {UP: LEFT, RIGHT: DOWN},
    4: {DOWN: LEFT, RIGHT: UP},
    5: {}
}


