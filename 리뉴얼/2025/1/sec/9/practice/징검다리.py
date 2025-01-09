def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = right
    while left <= right:
        temp_cnt = 0
        prev_rock = min(rocks)
        mid = (left + right) // 2
        for rock in rocks:
            if rock - prev_rock < mid:
                temp_cnt += 1
            else:
                prev_rock = rock
        
        if temp_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer