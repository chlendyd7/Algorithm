from collections import deque


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(0,1), (1,0)]

q = deque([(0,0, board[0][0])])
visited = set()
visited.add((0,0))
can_do = False
while q:
    nx, ny, dir = q.popleft()
    if board[nx][ny] == -1:
        print('HaruHaru')
        can_do = True
        break

    for dx, dy in direction:
        xx, yy = nx + (dx * dir), ny + (dy * dir)
        if 0<= xx < n and 0<= yy < n:
            if (xx,yy) not in visited:
                q.append((xx,yy,board[xx][yy]))
                visited.add((xx,yy))



if not can_do:
    print('Hing')