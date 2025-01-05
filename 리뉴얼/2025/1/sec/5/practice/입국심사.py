def solution(n, times):
    start = 0
    end = max(times) * n
    answer = end
    while start <= end:
        mid = (start + end) // 2
        total = sum(mid // time for time in times)
        
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
