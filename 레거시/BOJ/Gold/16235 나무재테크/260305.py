from collections import deque
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

input = sys.stdin.readline

N,M,K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

for r in range(N):
    for c in range(N):
        if trees[r][c]:
            trees[r][c] = deque(sorted(trees[r][c]))

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(K):
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue

            alive_trees = deque()
            dead_tree = 0

            while trees[r][c]:
                age = trees[r][c].popleft()
                if board[r][c] >= age:
                    board[r][c] -= age
                    alive_trees.append(age+1)
                else:
                    dead_tree += (age // 2)

            trees[r][c] = alive_trees
            board[r][c] += dead_tree
    
    for r in range(N):
        for c in range(N):
            for age in trees[r][c]:
                if age % 5 == 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0<= nr < N and 0 <= nc < N:
                            trees[nr][nc].appendleft(1)
            
            board[r][c] += A[r][c]

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])
print(answer)
