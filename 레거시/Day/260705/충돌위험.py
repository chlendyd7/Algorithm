from collections import Counter

def solution(points, routes):
    # 1. 모든 로봇의 '초 단위 위치 경로'를 담을 리스트
    # robot_paths[i] = i번째 로봇의 [0초 좌표, 1초 좌표, 2초 좌표, ...]
    robot_paths = []
    
    for route in routes:
        path = []
        # 첫 번째 시작점 위치를 넣어줍니다. (0초)
        start_point = points[route[0] - 1]
        path.append(tuple(start_point))
        
        # 순서대로 다음 경유지들을 방문
        for i in range(len(route) - 1):
            curr = list(points[route[i] - 1])
            nxt = points[route[i+1] - 1]
            
            # 다음 목적지(nxt)에 도착할 때까지 한 칸씩 이동하며 기록
            while curr != nxt:
                # r 좌표 먼저 이동
                if curr[0] != nxt[0]:
                    curr[0] += 1 if curr[0] < nxt[0] else -1
                # r 좌표가 같아지면 c 좌표 이동
                elif curr[1] != nxt[1]:
                    curr[1] += 1 if curr[1] < nxt[1] else -1
                
                path.append(tuple(curr))
                
        robot_paths.append(path)
    
    # 2. 모든 로봇의 경로를 다 구했으니, 시간(초)별로 겹치나 확인!
    result = 0
    max_time = max(len(p) for p in robot_paths) # 가장 길게 움직인 로봇의 시간
    
    for t in range(max_time):
        positions_at_t = []
        for path in robot_paths:
            # 해당 시간에 로봇이 아직 이동 중이라면 위치를 추가
            if t < len(path):
                positions_at_t.append(path[t])
        
        # 현재 시간(t초)에 각 좌표에 로봇이 몇 대 있는지 세어줍니다.
        '''
        Counter를 거치면 다음과 같이 깔끔하게 정리가 됩니다.
        {(4,4): 2개, (1,2): 1개, (5,5): 1개}
        '''
        
        count = Counter(positions_at_t)
        for pos, cnt in count.items():
            if cnt >= 2: # 2대 이상 모여있다면 위험 상황!
                result += 1
                
    return result