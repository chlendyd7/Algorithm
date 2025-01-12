def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    left = 1
    right = distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        temp_cnt = 0
        prev_rock = 0
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
