def solution(t, p):
    p_len = len(p)
    answer = 0
    
    for i in range(len(t) - p_len + 1):  # 가능한 시작 지점 반복
        if int(t[i:i + p_len]) <= int(p):  # 부분 문자열을 정수로 변환 후 비교
            answer += 1
            
    return answer
