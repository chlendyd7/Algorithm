def solution(a):
    answer = 2
    N = len(a)
    min_left, min_right = [0] * N, [0] * N
    
    min_left[0] = a[0]
    for i in range(1, N):
        min_left[i] = min(min_left[i-1], a[i])

    min_right[N-1] = a[N-1]
    for i in range(N-2, -1, -1):
        min_right[i] = min(a[i], min_right[i+1])
    
    for i in range(1, N-1):
        if a[i] <= min_left[i] or a[i] <= min_right[i]:
            answer += 1

    return answer