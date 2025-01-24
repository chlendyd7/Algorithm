from collections import defaultdict


def solution(arrows):
    dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    visit = defaultdict(list)
    x,y = 0,0

    for arrow in arrows:
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x,y))
            elif (nx, ny) not in visit:
                visit[(x, y)].append((nx, ny))

    answer = 0
    return answer
