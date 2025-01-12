def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    answer = distance
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        last_rock = rocks[0]
        temp_cnt = 0
        for rock in rocks:
            if rock - last_rock < mid:
                temp_cnt += 1
                last_rock = rock
            else:
                last_rock = rock
        
        if temp_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer