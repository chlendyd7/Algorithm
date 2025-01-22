def solution(stones, k):
    answer = 0

    left, right = 0, max(stones)
    while left <= right:
        mid = (left + right) // 2
        check = 0
        for stone in stones:
            if stone <= mid:
                check += 1
                if check >= k:
                    break
            else:
                check = 0
        
        if check == k:
            right = mid - 1
        else:
            left = mid + 1

    return left
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))