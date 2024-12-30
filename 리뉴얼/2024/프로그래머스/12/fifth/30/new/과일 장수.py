from collections import Counter

def solution(k, m, score):
    counter = Counter(score)
    counter_lst = sorted(counter.items(), key=lambda x: -x[0])
    
    answer = 0
    current_box = []

    for price, num in counter_lst:
        while num > 0:
            current_box.append(price)
            num -= 1
            
            if len(current_box) == m:
                answer += min(current_box) * m
                current_box = []

    return answer
