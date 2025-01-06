def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()

    left, right = 0, distance


    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        prev_rock = min(rocks)
        for r in rocks:
            if r - prev_rock < mid:
                cnt += 1
            else:
                prev_rock = r

        if cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer