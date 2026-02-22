def check(row, col):
    return 0<= row < R and 0<= col < C

def dfs(x,y,count):
    global answer
    answer = max(answer, count)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if check(nx,ny):
            if board[nx][ny] not in alpha:
                alpha.add(board[nx][ny])
                dfs(nx,ny,count+1)
                alpha.remove(board[nx][ny])


dx = [1,0,-1,0]
dy = [0,1,0,-1]

R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]
alpha = set()
visitied = [[False] * C for _ in range(R)]
alpha.add(board[0][0])
visitied[0][0] = 1
answer = 0
dfs(0,0,1)
print(answer)
