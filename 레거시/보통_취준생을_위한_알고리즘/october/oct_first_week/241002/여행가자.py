from collections import deque


def bfs(s,e):
    q = deque()
    q.append(s)
    visited = [False] * n
    visited[s] = True

    while q:
        here = q.popleft()

        if here == e:
            return True
        for i in range(n):
            if graph[here][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return False

n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
target = list(map(int,input().split()))

answer = True
for i in range(m-1):
    if target[i] != target[i+1]:
        if not bfs(target[i] -1, target[i+1] - 1):
            answer = False
            break

if answer:
    print('YES')
else:
    print('NO')
