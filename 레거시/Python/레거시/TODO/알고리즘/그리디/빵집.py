import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  if y == m - 1:
    return True

  for i in range(3):
    nx = x + dx[i]
    ny = y + 1
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
      graph[nx][ny] = 'x'
      if dfs(nx, ny):
        return True
  return False

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

dx = [-1, 0, 1]
answer = 0

for x in range(n):
  if dfs(x, 0):
    answer += 1

print(answer)