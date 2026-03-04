'''
    N,N 크기 r,c 는 1부터 시작, 가장 처음 양분은 모든 칸에 5만큼 들어가있음
    M개의 나무를 구매해 땅에 심음, 
    봄 => 자신의 나이만큼 양분을 먹고 나이가 1 증가
    하나의 칸에 여러개의 나무가 있을 수 있음, 나이가 어린 나무부터 양분을 먹음, 양분이 부족해 못먹으면 즉시 죽음
    여름 => 죽은 나무가 양분으로 변함, 나이를 2로 나눈 값
    가을 => 나무가 번식함, 번식하려면 나무의 나이가 5배수 인접한 8개의 칸에 나이가 1인 나무가 생김
    겨울= => 양분 추가, A[r][c]양분이 각 칸에 추가됨
    K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하라
'''
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


from collections import defaultdict


N, M, K = map(int, input().split())
a_board = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
trees = defaultdict(list)

def spring():
    dead = []
    for r,c in trees.keys():
        tree = trees[(r,c)]
        yangbun = board[r][c]
        if len(tree) >= 2:
            tree.sort()

        for i in range(len(tree)):
            if yangbun < tree[i]:
                trees[(r,c)] = tree[:i]
                dead.append((r,c, sum(s//2 for s in tree[i:])))
            else:
                yangbun -= tree[i]
                tree[i] += 1
        board[r][c] = yangbun
    return dead

def summer(dead):
    for r,c, z in dead:
        board[r][c] += z
        if not trees[(r,c)]:
            del trees[(r,c)]

direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def fall():
    append_list = []
    for key, value in trees.items():
        for tree in value:
            if tree % 5 == 0:
                append_list.append((key))

    for r,c in append_list:
        for dr, dc in direction:
            nr, nc = r+dr, c+dc
            if 0<= nr < N and 0 <= nc < N:
                trees[(nr,nc)].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += a_board[i][j]


for _ in range(M):
    x,y,z = map(int, input().split())
    # 작은 것 부터 먹는걸 구현해야하는데 sort를 해야하나?
    # M은 100 x 1000 x 10 탐색 범위 쫍나? 이거 물어보자
    trees[(x-1,y-1)].append(z)

for _ in range(K): #k 번 반복
    dead = spring()
    summer(dead)
    fall()
    winter()
    print(_, board)
    print('tree:', trees)

cnt = 0
print(trees)
for item, value in trees.items():
    cnt += len(value)

print(cnt)
