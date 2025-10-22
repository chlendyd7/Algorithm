def solution(sequence, k):
    start, end = 0, 0
    s_len = len(sequence)
    min_len = 1000000
    answer = []
    sum_sequence = 0
    while start <= s_len:
        if sum_sequence > k:
            sum_sequence -= sequence[start]
            start += 1
        else:
            if sum_sequence == k:
                if end + 1 - start < min_len:
                    answer = [start, end - 1]
                    min_len = end - start + 1
            if end < len(sequence):
                sum_sequence += sequence[end]
                end += 1
            else:
                break

    return answer