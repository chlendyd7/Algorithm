def solution(park, routes):
    direction = {
        'N' : (-1, 0),
        'S' : (1, 0),
        'W' : (0, -1),
        'E' : (0, 1)
    }
    H, W = len(park), len(park[0])
    start = None

    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start = [i,j]
                break
        if start:
            break
    
    x,y = start
    for route in routes:
        dir, dis = route.split()
        dis = int(dis)
        dx, dy = direction[dir]

        nx, ny = x, y
        valid = True
        for _ in range(dis):
            nx, ny = nx + dx, ny + dy
            if not(0<= nx < H and 0<= ny < W) or park[nx][ny] == 'X':
                valid = False
                break
        
        if valid:
            x, y = nx, ny

    answer = [x, y]
    return answer