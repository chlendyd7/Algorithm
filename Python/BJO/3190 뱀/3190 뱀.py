from collections import defaultdict, deque
# import os
# import sys


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')
LEFT = "L"
RIGHT = "D"
DIRECTION = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]
N = int(input())
K = int(input())
apples = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    apples[r-1][c-1] = 1
L = int(input())
cmd = defaultdict() # key value 담아둠
for _ in range(L):
    inputs = input().split()
    cmd[int(inputs[0])] = inputs[1]

# 몸 길이를 기록하고 해당 방향 -= dr * 몸길이 만큼의 범위에 머리가 도달하는지만 체크하면 될 것 같은데
# 해당 방법은 꺾어지는 경우에 같이 몸이 따라오기에 불가능
# 큐에 넣어다니면서 체크하기

# 선형탐색
# 시뮬레이션 해도 될 듯, 다른방법이 있으면 찾아보기

cnt = 0
r, c, = 0, 0
direct = 0
q = deque([(0,0)])
eat = False
while True:
    cnt += 1
    dr, dc = DIRECTION[direct]
    r, c = r + dr, c + dc
    if cnt in cmd:
        if cmd[cnt] == RIGHT:
            direct = (direct + 1) % 4
        elif cmd[cnt] == LEFT:
            if direct == 0:
                direct = 3
            else:
                direct -=1
    if r < 0 or r >= N or c < 0 or c >= N:
        break

    if (r, c) in q:
        break


    if apples[r][c]:
        apples[r][c] = 0
        q.append((r-dr, c-dc))

    q.append((r,c))
    q.popleft()



print(cnt)
