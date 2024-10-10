import sys


sys.setrecursionlimit(10000)
def check(x, y, row, col):
    return 0 <= x < col and 0 <= y < row


dy = [1,0,-1]

def dfs(x,y):
    if x == C - 1:
        return True
    
    for i in range(3):
        nx = x + 1
        ny = y + dy[i]
        if check(nx, ny, C, R):
            if graph[ny][nx] == '.':
                graph[ny][nx] = 'x'
                if dfs(nx, ny):
                    return True
    return False




R,C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
cnt = 0
for y in range(R):
    if dfs(0,y):
        cnt += 1
print(cnt)
