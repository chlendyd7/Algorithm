from itertools import combinations_with_replacement

def solution(n, info):
    max_diff = 0
    answer = [-1]
    
    # 라이언이 쏠 수 있는 점수 조합 생성
    for comb in combinations_with_replacement(range(11), n):
        lion = [0] * 11
        for c in comb:
            lion[10 - c] += 1
        
        # 점수 계산
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if info[i] >= lion[i]:
                apeach_score += 10 - i
            else:
                lion_score += 10 - i
        
        diff = lion_score - apeach_score
        
        # 점수 차이가 더 크거나, 점수가 낮은 쪽을 우선시
        if diff > max_diff or (diff == max_diff and lion[::-1] > answer[::-1]):
            max_diff = diff
            answer = lion
    
    return answer if max_diff > 0 else [-1]
