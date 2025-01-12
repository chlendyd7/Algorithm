def solution(park, routes):
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    h, w = len(park), len(park[0])
    start = None
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                start = [i,j]
                break
        if start:
            break

    x, y = start
    for route in routes:
        dir, dist = route.split()
        dx, dy = directions[dir]
        dist = int(dist)
        
        nx, ny = x, y
        valid = True
        for i in range(dist):
            nx, ny = nx + dx, ny + dy
            if not (0<= nx < h and 0<= ny < w) or park[nx][ny] == "X":
                valid = False
                break
        
        if valid:
            x, y = nx, ny

    return [x, y]
