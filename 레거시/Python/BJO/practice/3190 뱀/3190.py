from collections import defaultdict, deque


LEFT = 'L'
RIGHT = 'D'
DIRECTION = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
N = int(input())
K = int(input())
apples = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    apples[r-1][c-1] = 1

L = int(input())
cmd = defaultdict()
for _ in range(L):
    inputs = input().split()
    cmd[int(inputs[0])] = inputs[1]

cnt = 0
r, c = 0,0
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
                direct -= 1
    if r < 0 or r >= N or c < 0 or c >= N:
        break
    
    if (r, c) in q:
        break
    
    if apples[r][c]:
        apples[r][c] = 0
        q.append((r,c))
    else:
        q.append((r,c))
        q.popleft()

print(cnt)
