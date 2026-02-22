def solution(n, times):
    # 이분 탐색 범위 설정
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2  # 현재 시점에서의 최대 시간
        total = sum(mid // time for time in times)  # mid 시간 동안 심사 가능한 사람 수
        
        if total >= n:  # 심사 가능 인원이 목표보다 많거나 같으면
            answer = mid  # 일단 정답 후보로 저장
            right = mid - 1  # 시간을 줄여 더 최적화된 답을 찾음
        else:  # 심사 가능 인원이 목표보다 적으면
            left = mid + 1  # 시간을 늘려야 더 많은 사람을 심사 가능
            
    return answer
