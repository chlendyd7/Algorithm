def solution(n, times):
    left, right = 0, max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        total_cnt = sum([mid // time for time in times])

        if total_cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer