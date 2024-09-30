from collections import deque

def dfs(x,y, count):
    global answer

    answer = max(answer, count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx <r and 0<= ny < c and board[nx][ny] not in alpha:
            alpha.add(board[nx][ny])
            dfs(nx,ny,count+1)
            alpha.remove(board[nx][ny])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

r, c = map(int,input().split())
alpha = set()
board = [list(input()) for _ in range(r)]
alpha.add(board[0][0])
answer = 0

dfs(0,0,1)
print(answer)
