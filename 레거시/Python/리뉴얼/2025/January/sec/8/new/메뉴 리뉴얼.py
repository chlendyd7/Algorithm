from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = Counter()
        for order in orders:
            # 조합 생성 후 정렬된 문자열로 변환
            comb_counter.update([''.join(sorted(comb)) for comb in combinations(order, c)])
        
        if comb_counter:
            max_count = max(comb_counter.values())
            if max_count >= 2:
                # 등장 횟수가 최대값인 조합을 추가
                answer.extend([comb for comb in comb_counter if comb_counter[comb] == max_count])

    return sorted(answer)
