from collections import Counter

def solution(k, m, score):
    counter = Counter(score)
    counter_lst = sorted(counter.items(), key=lambda x: -x[0])
    
    answer = 0
    current_box = []  # 현재 상자에 담긴 사과 점수

    for price, num in counter_lst:
        while num > 0:  # 현재 점수 그룹의 사과를 처리
            current_box.append(price)
            num -= 1
            
            # 상자가 꽉 찼을 때 처리
            if len(current_box) == m:
                answer += min(current_box) * m
                current_box = []  # 상자를 초기화

    return answer
