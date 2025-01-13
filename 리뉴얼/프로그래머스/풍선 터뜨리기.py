from collections import deque


def solution(a):
    answer = 2
    n = len(a)
    
    left_min = [0] * n
    right_min = [0] * n
    
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
    
    for i in range(1, n-1):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    return answer


def solution(a):
    if len(a) <= 2:  # 풍선이 2개 이하라면 모든 풍선을 터뜨릴 수 있음
        return len(a)
    
    answer = 2  # 첫 번째와 마지막 풍선은 항상 남길 수 있음
    N = len(a)

    # 왼쪽 최소값과 오른쪽 최소값을 기록
    min_left, min_right = [0] * N, [0] * N
    
    min_left[0] = a[0]
    for i in range(1, N):
        min_left[i] = min(min_left[i-1], a[i])
    
    min_right[N-1] = a[N-1]
    for i in range(N-2, -1, -1):
        min_right[i] = min(a[i], min_right[i+1])
    
    # 첫 번째와 마지막은 이미 포함되어 있으므로 1 ~ N-2까지 확인
    for i in range(1, N-1):
        if a[i] > min_left[i-1] and a[i] > min_right[i+1]:
            continue  # 양쪽에서 더 작은 값이 있으므로 이 풍선은 남길 수 없음
        answer += 1

    return answer
