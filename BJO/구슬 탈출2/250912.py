from collections import deque
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

N, M = map(int, input().split())
board = []
red, blue = None, None
for i in range(N):
    row = list(input())
    board.append(row)
    for j in range(M):
        if row[j] == 'B':
            blue = (i, j)
        elif row[j] == 'R':
            red = (i, j)

DIRECTION = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]
visited_set = set()
visited_set.add((*red, *blue))

def move(r, c, dr, dc):
    nr, nc = r + dr, c + dc
    cnt = 0
    while board[nr][nc] != '#' and board[r][c] != 'O':
        cnt += 1
        r, c = nr, nc
        nr, nc = r + dr, c + dc
    return cnt, r, c


q = deque([(0, *red, *blue)])
while q:
    depth, rr, rc, br, bc = q.popleft()
    if depth > 10:
        break
    

    for dr, dc in DIRECTION:
        rcnt, nrr, nrc = move(rr, rc, dr, dc)
        bcnt, nbr, nbc = move(br, bc, dr, dc)

        if board[nbr][nbc] == 'O':
            continue
        
        if board[nrr][nrc] == 'O':
            print(depth)
            break

        if nrr == nbr and nrc == nbc:
            if rcnt > nbc:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc

        if (nrr, nrc, nbr, nbc) in visited_set:
            continue
        visited_set.add((nrr,nrc,nbr,nbc))
        q.append((depth+1, nrr, nrc, nbr, nbc))



print(red, blue, board)
