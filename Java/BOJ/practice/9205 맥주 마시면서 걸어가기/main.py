from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    store = []
    for _ in range(n):
        x,y = map(int,input().split())
        store.append((x,y))
    ex, ey = map(int,input().split())
    q = deque([(sx, sy)])
    visited = [0] * n
    find = False

    while q:
        current = q.popleft()
        
        x, y = current[0], current[1]

        if abs(x - ex) + abs(y - ey) <= 1000:
            print('happy')
            find = True
            break

        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = True

    if not find:
        print('sad')
