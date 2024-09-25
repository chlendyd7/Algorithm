

import heapq


def solution(n, board):
    q = []
    heapq.heappush(q, (0,0,board[0][0]))
    dis = [[1e9] * n for _ in range(n)]
    while q:
        x, y, distance = heapq.heappop(q)
        
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance}')
            n = int(input())
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n:
                cost = board[nx][ny]
                if dis[nx][ny] > cost:
                    dis[nx][ny] = cost
                    heapq.heappush(q, (nx,ny,cost))
            
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
cnt = 0
while n:
    cnt += 1
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    q = []
    heapq.heappush(q, (0,0,board[0][0]))
    dis = [[1e9] * n for _ in range(n)]
    dis[0][0] = board[0][0]

    while q:
        x, y, distance = heapq.heappop(q)
        
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {distance}')
            n = int(input())
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n:
                cost = distance + board[nx][ny]
                if dis[nx][ny] > cost:
                    dis[nx][ny] = cost
                    heapq.heappush(q, (nx,ny,cost))
