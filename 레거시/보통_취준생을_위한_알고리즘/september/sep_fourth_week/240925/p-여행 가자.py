from collections import deque


n = int(input())
m = int(input())
city = [list(map(int,input().split())) for _ in range(n)]
target = list(map(int, input().split()))

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [False] * n
    visited[start] = True

    while q:
        here = q.popleft()

        if here == end:
            return True
        
        for i in range(n):
            if city[here][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    return False


answer = True
for i in range(m-1):
    if target[i] != target[i+1]:
        if not bfs(target[i]-1, target[i+1]-1):
            answer = False
            break


if answer:
    print('YES')
else:
    print('NO')