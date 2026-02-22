def solution(park, routes):
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
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
        way, lang = route.split(' ')
        lang = int(lang)

        check = True
        nx, ny = x, y
        dx, dy = direction[way]
        for _ in range(lang):
            nx += dx
            ny += dy
            if not(0<= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                check = False
        if check:
            x += (dx * lang)
            y += (dy * lang)


    return [x,y]

solution(["SOO","OOO","OOO"],	["E 2","S 2","W 1"])