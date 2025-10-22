def solution(sequence, k):
    start, end = 0, 0
    min_len = float('inf')
    sum_sequence = 0
    answer = []

    while start < len(sequence):  # 수정: 배열의 범위를 초과하지 않도록 조건 변경
        if sum_sequence > k:
            sum_sequence -= sequence[start]
            start += 1
        else:
            if sum_sequence == k:
                if end - start + 1 < min_len:  # 수정: 최소 길이를 추적하기 위해 부등호 변경
                    answer = [start, end - 1]  # 수정: end가 이미 증가했으므로 end - 1로 기록
                    min_len = end - start + 1
            if end < len(sequence):  # 수정: end가 배열 범위를 초과하지 않도록 조건 추가
                sum_sequence += sequence[end]
                end += 1
            else:
                break
    
    return answer