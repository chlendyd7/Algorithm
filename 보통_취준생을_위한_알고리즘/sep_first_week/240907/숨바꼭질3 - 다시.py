from collections import deque

def bfs(x,y) :
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == y:
            return
        for nx in (2*x, x-1, x+1):
            if 0 < nx <= max and not visited[nx]:
                if nx == x * 2:
                    visited[nx] = visited[x]
                else:
                    visited[nx] = visited[x] + 1

                q.append(nx)


n,k = map(int,input().split())
max = 10**5
visited = [0] * (max+1)
bfs(n,k)
print(visited[k] - 1)