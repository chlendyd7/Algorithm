import heapq
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
cnt = 0
while n:
    cnt += 1
    board = [list(map(int,input().split())) for _ in range(n)]
    heap = []
    dis = [[sys.maxsize] * n for _ in range(n)]
    heapq.heappush(heap, (board[0][0], 0,0))
    dis[0][0] = board[0][0]
    while heap:
        distance, y, x = heapq.heappop(heap)
        
        if y == n-1 and x == n-1:
            print("Problem", str(cnt)+":", distance)
            n = int(input())
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<= nx < n and 0 <= ny < n:
                cost = distance + board[ny][nx]
                if dis[ny][nx] > cost:
                    dis[ny][nx] = cost
                    heapq.heappush(heap, (cost, ny, nx))
