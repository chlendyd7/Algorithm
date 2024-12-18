def solution(park, routes):
    # 1. 공원 정보 초기화
    H, W = len(park), len(park[0])
    start = None
    
    # 시작 위치 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                start = [i, j]
                break
        if start:
            break

    # 방향 정의
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    
    # 2. 명령 수행
    x, y = start
    for route in routes:
        dir, dist = route.split()
        dx, dy = directions[dir]
        dist = int(dist)
        
        # 이동 가능 여부 확인
        nx, ny = x, y
        valid = True
        for _ in range(dist):
            nx, ny = nx + dx, ny + dy
            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                valid = False
                break
        
        # 이동 가능한 경우만 실제 이동
        if valid:
            x, y = nx, ny
    
    # 3. 결과 반환
    return [x, y]
