r,c = map(int,input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))

ans = 0
alpha = set()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < r and 0<= ny < c and not maps[nx][ny] in alpha:
            alpha.add(maps[nx][ny])
            dfs(nx,ny,count+1)
            alpha.remove(maps[nx][ny])

alpha.add(maps[0][0])
dfs(0,0,1)
print(ans)
