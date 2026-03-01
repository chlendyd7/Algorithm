from collections import deque
import sys
import os

# 로컬에서 테스트할 때만 주석 해제
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')

input = sys.stdin.readline
print(input)

'''
   N,M 크기 격자판 적의 수는 최대 1
   N+1 모든 칸에 성이 있음
   궁수 3명을 배치, 한 명만 배치
   턴마다 하나를 공격 (동시)
   D 이하인 적 중에서 가장 가까운 적, 가장 왼쪽 부터
   같은 적 여러 궁수에게 공격 당할 수 있음
   적 이동 -> 아래로 한 칸 이동
   성에 도달하면 게임에서 제외, 모든 적 격자판 제외되면 게임 끝 

   (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|

    궁수의 공격으로 제거할 수 있는 적의 최대 수
    완탐
    
    배치, 가장 왼쪽 공격하는 시뮬, 적 이동 시뮬, 게임 제외 시뮬, end 시뮬
'''
from itertools import combinations
N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0


def simulation(archurs, targets):
    curr_targets = copy.deepcopy(targets)
    
    cnt = 0
    while curr_targets:
        targets_to_die = set()
        # 잡는 시뮬레이션

        for archur in archurs:
            best_target = None
            min_dist = D + 1
            for i in range(len(curr_targets)):
                r, c = curr_targets[i]
                dist = abs(N-r) + abs(archur - c)
                if dist <= D:
                    if dist < min_dist:
                        min_dist = dist
                        best_target = i
                    elif dist == min_dist:
                        if c < curr_targets[best_target][1]:
                            best_target = i
                
            if best_target is not None:
                targets_to_die.add(tuple(curr_targets[best_target]))
        
        for die in targets_to_die:
            curr_targets = [t for t in curr_targets if tuple(t) != die]
            cnt += 1
        
        new_targets = []
        for r, c in curr_targets:
            if r + 1 < N:
                new_targets.append([r+1, c])
        curr_targets = new_targets

    return cnt

import copy
targets = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            targets.append([r,c])

max_kill = 0
for archurs in combinations(range(M), 3):
    max_kill = max(max_kill, simulation(archurs, targets))
print(max_kill)








print("\n=== 정답지 (output.txt) ===")
output_path = os.path.join(current_dir, 'output.txt')

if os.path.exists(output_path):
    # 여기서 encoding='utf-8'을 넣어주면 에러가 사라집니다!
    with open(output_path, 'r', encoding='utf-8') as f:
        print(f.read().strip())
else:
    print("output.txt 파일이 없습니다!")