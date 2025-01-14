def solution(elements):
    result = set()
    element_len = len(elements)
    
    # 원형 배열을 처리하기 위해 두 번 반복된 배열 생성
    elements = elements * 2
    
    # 슬라이딩 윈도우로 합 계산
    for length in range(1, element_len + 1):
        current_sum = sum(elements[:length])  # 초기 윈도우 합
        result.add(current_sum)
        
        for start in range(1, element_len):  # 윈도우 이동
            current_sum += elements[start + length - 1] - elements[start - 1]
            result.add(current_sum)
    
    return len(result)
