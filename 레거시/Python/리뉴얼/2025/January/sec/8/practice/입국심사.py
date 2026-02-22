def solution(n, times):
    times.sort()
    left, right = 0, times[-1] * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        result = [mid // t for t in times]
        if sum(result) >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer