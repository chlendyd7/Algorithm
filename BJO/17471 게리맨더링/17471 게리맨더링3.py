from collections import deque


n = int(input())
people = list(map(int, input().split()))

def bfs(g):
    q = deque()
    check = [False for _ in range(n)]
    q.append(g[0])
    check[g[0]] = True

    cnt, answer = 1, 0
    while q:
        temp = q.popleft()
        answer += people[temp]
        for i in board[temp]:
            if i in g and not check[i]:
                check[i] = True
                cnt += 1
                q.append(i)

def dfs(cnt, x, end):
    global min_value

    if cnt == end:
        g1, g2 = deque(), deque()

        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)

        ans1 = bfs(g1)
        if not ans1:
            return
        
        ans2 = bfs(g2)
        if not ans2:
            return
        

board = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        board[i].append(j-1)

min_value = 1e9
for i in range(1, n//2 + 1):
    visited = [False for _ in range(n)]
    dfs(0, 0, i)

if min_value == 1e9:
    print(-1)
else:
    print(min_value)