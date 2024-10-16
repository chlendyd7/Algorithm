pip = [-1,0,1]

def dfs(x,y):
    if y == C - 1:
        return True
    
    for i in range(3):
        nx = x + pip[i]
        ny = y + 1
        if 0<= nx < R and 0<= ny < C and graph[nx][ny] == '.':
            graph[nx][ny] = 'x'
            if dfs(nx,ny):
                return True
    return False


R, C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
answer = 0

for i in range(R):
    if dfs(i,0):
        answer += 1
print(answer)
