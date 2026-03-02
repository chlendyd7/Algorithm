from collections import defaultdict
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
'''

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
curr = [0,0]
fish_dict = defaultdict(list)
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            curr = [r,c]
        elif board[r][c] != 0:
            fish_dict[board[r][c]].append((r,c))


# while fish_dict:
#     for 
print(fish_dict, curr)