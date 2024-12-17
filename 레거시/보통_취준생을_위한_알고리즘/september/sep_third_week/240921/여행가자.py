from collections import deque


n = int(input())
m = int(input())

city = []
for i in range(n):
    city.append(list(map(int,input().split())))
plan = list(map(int,input().split()))

def bfs(s, e):
    q = deque()
    q.append(s)
    visited = [False] * n
    visited[s] = True
    
    while q:
        now = q.popleft()
        if now == e:
            return True
        
        for i in range(n):
            if city[now][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return False


answer = True
for i in range(m-1):
    if not plan[i] != plan[i+1]:
        if bfs(plan[i]-1, plan[i+1] - 1):
            answer = False
            break
