pip = [-1,0,1]

def dfs(x,y):
    if y == m - 1:
        return True
    
    for i in range(3):
        nx = x + pip[i]
        ny = y + 1
        if 0<= nx < n and 0<= ny < m and graph[nx][ny] == '.':
            graph[nx][ny] = 'x'
            if dfs(nx,ny):
                return True
    return False



n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
answer = 0

for i in range(n):
    if dfs(i,0):
        answer += 1
print(answer)