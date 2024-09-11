from collections import deque


def solution(n,k):
    q = deque([n])
    visited[n] = 1
    while q:
        now = q.popleft()
        if now == k:
            return
        for nx in (now*2, now-1, now+1):
            if 0 < nx <= max and not visited[nx]:
                if nx == now * 2:
                    visited[nx] = visited[now]
                else:
                    visited[nx] = visited[now] + 1
                
                q.append(nx)
        
        
n,k = map(int,input().split())
max = 100000
visited = [0] * (max + 1)
solution(n,k)
print(visited[k] - 1)
