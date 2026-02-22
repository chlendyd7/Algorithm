import heapq
import sys


dx = [1,0,-1,0]
dy = [0,1,0,-1]


n = int(input())
cnt = 0
q = []
while n:
    cnt += 1
    board = [list(map(int,input().split())) for _ in range(n)]
    dis = [[sys.maxsize] * n for _ in range(n)]
    heapq.heappush(q,(0,0,board[0][0]))
    dis[0][0] = 1

    while q:
        x,y,distance = heapq.heappop(q)
        if x == n-1 and y== n-1:
            print(f"Problem {cnt}: {distance}")
            n = int(input())
            break
        
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny < n:
                    cost = distance + board[nx][ny]
                    if dis[nx][ny] > cost:
                        dis[nx][ny] = cost
                        heapq.heappush(q, (nx,ny,cost))
