def solution(sequence, k):
    start, end = 0, 0
    answer = []
    sum_value = 0
    min_len = 1000000
    while start < len(sequence):
        if sum_value > k:
            sum_value -= sequence[start]
            start += 1
        else:
            if sum_value == k:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    answer = [start, end-1]
            if end < len(sequence):
                sum_value += sequence[end]
                end += 1
            else:
                break

    return answer


def solution(sequence, k):
    start, end = 0, 0
    answer = []
    sum_value = 0
    min_len = float('inf')

    while end < len(sequence):
        sum_value += sequence[end]
        while sum_value > k and start <= end:
            sum_value -= sequence[start]
            start += 1
        if sum_value == k:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start, end]
        end += 1

    return answer
