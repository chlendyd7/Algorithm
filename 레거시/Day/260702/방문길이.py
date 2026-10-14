# https://school.programmers.co.kr/learn/courses/30/lessons/49994
'''
좌표 사용하면서 map으로 매핑해두고
좌표를 set에 넣어서 최종 길이 구하기
좌표는 늘 짧은곳에서 긴곳으로 정렬해서 넣기?
((짧,긴), (짧,긴)) 이렇게 되나?
'''

cmd = {
    "U": (1,0),
    "D": (-1,0),
    "L": (0,-1),
    "R": (0,1)
}

def solution(dirs):
    dir = set()
    x, y = 0,0
    
    for d in dirs:
        dx, dy = cmd[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            dir.add(((max(nx, x), min(nx, x)),(max(ny, y), min(ny, y))))
            x = nx
            y = ny
    return len(dir)


def solution(dirs):
    # set의 이름을 더 명확하게 (visited_paths)
    visited_paths = set()
    x, y = 0, 0
    
    # 명령어 정의
    cmd = {
        "U": (0, 1),  # 보통 좌표계에서 U는 y+1
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }
    
    for d in dirs:
        dx, dy = cmd[d]
        nx, ny = x + dx, y + dy
        
        # 범위 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 출발점과 도착점을 정렬하여 저장 (무방향 그래프의 간선 개념)
            path = tuple(sorted(((x, y), (nx, ny))))
            visited_paths.add(path)
            
            # 이동
            x, y = nx, ny
            
    return len(visited_paths)
