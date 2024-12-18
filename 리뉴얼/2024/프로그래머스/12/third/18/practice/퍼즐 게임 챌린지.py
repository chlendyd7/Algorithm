def solution(diffs, times, limit):
    def check_time(level):
        time = 0
        n = len(diffs)
        time_prev = 0
        for i in range(n):
            time_cur = times[i]
            cur_diff = diffs[i]
            if cur_diff <= level:
                time += time_cur
            else:
                wrong_attemps = cur_diff - level
                time += (time_cur + time_prev) * wrong_attemps + time_cur
            time_prev = time_cur

        return time

    left, right = 1, max(diffs)
    while left < right:
        mid = (left + right) // 2
        time_check = check_time(mid)
        if time_check <= limit:
            right = mid
        else:
            left = mid + 1

    
    return left
