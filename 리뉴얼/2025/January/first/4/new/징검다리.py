def solution(distance, rocks, n):
    # 돌을 정렬하고 끝 점 추가
    rocks.sort()
    rocks.append(distance)
    
    # 이분 탐색 범위 설정
    left, right = 0, distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2  # 최소 거리의 후보
        prev = 0  # 이전 돌의 위치
        removed = 0  # 제거한 돌의 개수
        
        # 각 돌의 위치를 확인하며 거리 계산
        for rock in rocks:
            if rock - prev < mid:  # 최소 거리보다 짧다면 돌 제거
                removed += 1
            else:
                prev = rock  # 돌을 유지하고 이전 위치 갱신
        
        if removed > n:  # 제거한 돌이 너무 많으면 거리 줄이기
            right = mid - 1
        else:  # 조건 만족 시 거리 늘리기
            answer = mid  # 정답 후보 갱신
            left = mid + 1
    
    return answer
