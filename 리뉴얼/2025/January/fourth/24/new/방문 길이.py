def solution(dirs):
    directions = {
        'U':(1,0),
        'D':(-1,0),
        'R':(0,1),
        'L':(0,-1)
    }

    visited = set()
    x, y = 0, 0
    cnt = 0
    for d in dirs:
        ny, nx = y + directions[d][0], x + directions[d][1]
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            path = ((x,y), (nx, ny))
            reverse_path = ((nx, ny), (x, y))
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                cnt += 1
            x, y = nx, ny

    return cnt