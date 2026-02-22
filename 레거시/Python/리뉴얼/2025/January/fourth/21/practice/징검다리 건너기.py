def solution(stones, k):
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        skip = 0
        
        for stone in stones:
            if stone <= mid:
                skip += 1
                if skip >= k:
                    break
            else:
                skip = 0
        if skip >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left
