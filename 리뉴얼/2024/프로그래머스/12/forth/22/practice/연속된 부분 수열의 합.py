def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')
    result = [-1, -1]

    while end < n:
        current_sum += sequence[end]
        end += 1

        while current_sum >= k:
            if current_sum == k:
                current_length = end - start
                if current_length < min_length:
                    min_length = current_length
                    result = [start, end - 1]
            current_sum -= sequence[start]
            start += 1
    
    return result