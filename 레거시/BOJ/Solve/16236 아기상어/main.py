from collections import defaultdict, deque
import sys
import os

# 로컬에서 테스트할 때만 주석 해제
# current_dir = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
# sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')

input = sys.stdin.readline
'''
    아기상어 크기 2 1초에 한칸씩 이동
    큰 물고기 있는 칸 지나갈 수 없음 나머지는 지나감
    작은 물고기 먹을 수 있음, 같으면 지나만 갈 수 ㅣㅆ음
    
    작은 물고기가 없으면 엄마 부름
    1 마리면 그 물고기 먹으로감, 여러마리는 가장 가까운 물고기 먹으로 감(지나야하는 칸 최소)
    (가장 위, 가장 왼쪽)
    크기와 같은 수의 물고기를 먹으면 크기 1 증가
    몇 초동안 엄마 상어에게 도움요청 하지 않고 물고기 잡아먹을 수 있을까요?
    BFS에 시뮬레이션
    9 아기상어 위치

    dict로 물고기 관리 크기 = [(r,c)]
    
    visited가 갱신되야함 먹었으면
    q를 다 돌고 먹고 반복
    q를 도는 함수 1개
    먹는 함수 하나 없으면 None 리턴
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
curr = [0,0]
fish_dict = defaultdict(list)
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            curr = [r,c]
            board[r][c] = 0
        else:
            continue
        break

# 좌표, 크기, 먹은 갯수
# visited를 거리로 쓸 수 도 있을 듯
# big, eat 글로벌 관리
def bfs(r, c):
    q = deque([(0,r,c)])
    visited = [[0]* N for _ in range(N)]
    visited[r][c] = True
    can_eat = [] # 먹을 수 있는 것
    while q:
        dist, r, c = q.popleft()
        if big > board[r][c] and board[r][c] != 0:
            can_eat.append((dist, r, c))

        for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and board[r][c] <= big:
                    q.append((dist+1, nr, nc))
                    visited[nr][nc] = 1

    return can_eat
# list로 먹을 수 있는거 return 하자

cnt = 0
c_r, c_c = curr[0], curr[1]
big, eat = 2, 0
while True:
    # list로 먹을 수 있는 것
    can_eat = bfs(c_r, c_c)
    if not can_eat:
        break
    else:
        # dist, r, c
        can_eat.sort()
        eat_fish = can_eat[0]
        cnt += eat_fish[0]
        c_r, c_c = eat_fish[1], eat_fish[2]
        eat += 1
        if big == eat:
            big += 1
            eat = 0
        board[c_r][c_c] = 0

print(cnt)