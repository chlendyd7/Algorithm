dx = [1,0,-1]

def dfs(x,y):
    if y == c-1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if 0<= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = 'x'
                if dfs(nx,ny):
                    return True
    return False



r,c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
cnt = 0
for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)
