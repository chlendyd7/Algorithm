from collections import deque


def solution(n, k):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        now = q.popleft()
        if n == k:
            return
        for nx in (now*2, now-1, now+1):
            if 0< nx <= 100000 and not visited[nx]:
                if nx == now*2:
                    visited[nx] = visited[n]
                else:
                    visited[nx] = visited[n] + 1
                q.append(nx)




n,k = map(int,input().split())
visited = [0] * 100001
solution(n,k)
print(visited[k])
