import sys


def solution(sequence, k):
    start, end = 0, 0
    answer = []
    sum_value = 0
    min_len = sys.maxsize

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