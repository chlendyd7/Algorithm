def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')
    result = [-1, -1]

    while end < n:
        # current_sum에 sequence[end]를 더하고 end를 증가시킴
        current_sum += sequence[end]
        end += 1

        # current_sum이 k 이상인 동안 start를 증가시키며 current_sum에서 sequence[start]를 뺌
        while current_sum >= k:
            if current_sum == k:
                current_length = end - start
                if current_length < min_length:
                    min_length = current_length
                    result = [start, end - 1]
            current_sum -= sequence[start]
            start += 1

    return result
