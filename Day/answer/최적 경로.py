from itertools import permutations

def solution():
    data = list(map(int, input().split()))
    n = data[0]
    
    # 1. 좌표 데이터 분리 (회사 -> 집 -> 고객 순서)
    cx, cy = data[1], data[2] # 회사
    hx, hy = data[3], data[4] # 집
    
    customers = [] # 고객 좌표
    for i in range(5, len(data), 2):
        customers.append((data[i], data[i+1]))
    
    min_dist = 1e9
    
    # 2. 순열을 통한 최적 경로 탐색
    for path in permutations(customers):
        temp_dist = 0
        curr_x, curr_y = cx, cy # 매 순열 시작 시 회사 좌표로 초기화
        
        for nx, ny in path:
            temp_dist += abs(curr_x - nx) + abs(curr_y - ny)
            curr_x, curr_y = nx, ny
            
        # 마지막 고객 위치 -> 집 이동 거리 추가
        temp_dist += abs(curr_x - hx) + abs(curr_y - hy)
        
        min_dist = min(min_dist, temp_dist)
        
    return min_dist

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')