def solution(diffs, times, limit):
    def calc_time(level):
        total_time = 0
        prev_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            if diff <= level:
                total_time += time_cur
                prev_time = time_cur
            else:
                wrong_attempts = diff - level
                total_time += (time_cur + prev_time) * wrong_attempts + time_cur
                prev_time = time_cur
        return total_time
    
    # Binary search for the minimum level
    left, right = 1, max(diffs)
    while left < right:
        mid = (left + right) // 2
        if calc_time(mid) <= limit:
            right = mid
        else:
            left = mid + 1
    return left
