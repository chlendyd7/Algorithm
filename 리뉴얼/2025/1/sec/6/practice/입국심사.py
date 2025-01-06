def solution(n, times):
    
    left, right = 0, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)

        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer