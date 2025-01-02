def solution(park, routes):
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    print(direction['N'])
    W,H = len(park[0]), len(park)
    start = []
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start = [i,j]
                break
        if start:
            break
    
    x,y = start

    for route in routes:
        r, cnt = route.split(' ')
        cnt = int(cnt)
        dx,dy = direction[r]
        
        check = True
        nx, ny = x, y

        for _ in range(cnt):
            nx, ny = nx + dx, ny + dy
            if not (0<= nx < H and 0<= ny < W) or park[nx][ny] == 'X':
                check = False
                break

        if check:
            x = nx
            y = ny

    return [x,y]

solution(["SOO","OOO","OOO"]	,["E 2","S 2","W 1"])