def solution(diffs, times, limit):
    
    def calculate(level):
        time = 0
        prev_time = 0
        n = len(diffs)
        for i in range(n):
            if diffs[i] <= level:
                time += times[i]
            else:
                time += (times[i] + prev_time) * (diffs[i] - level) + times[i]
            prev_time = times[i]

        return time

    left, right = 1, max(diffs)
    result = right

    while left <= right:
        mid = (left + right) // 2
        time = calculate(mid)
        if time <= limit:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
