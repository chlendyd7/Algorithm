r,c = map(int,input().split())
alpha = set()
lst = [list(input()) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0

def dfs(x,y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx <r and 0<= ny < c and lst[nx][ny] not in alpha:
            alpha.add(lst[nx][ny])
            dfs(nx,ny,count + 1)
            alpha.remove(lst[nx][ny])

alpha.add(lst[0][0])
dfs(0,0,1)

print(answer)
