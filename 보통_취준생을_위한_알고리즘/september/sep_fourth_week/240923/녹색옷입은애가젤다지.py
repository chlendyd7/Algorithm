import heapq


n = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
while n:
    cnt += 1
    board = [list(map(int,input().split())) for _ in range(n)]
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    dis = [[1e9] * n for _ in range(n)]
    dis[0][0] = board[0][0]
    
    while q:
        distance, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print("Problem", str(cnt)+":", distance)
            n = int(input())
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n:
                cost = distance + board[nx][ny]
                if dis[nx][ny] > cost:
                    dis[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
                
        
