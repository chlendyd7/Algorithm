from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = Counter()
        print(f"\n[DEBUG] Checking combinations of size {c}:")
        
        # 조합 생성 및 빈도 계산
        for order in orders:
            combs = [''.join(sorted(comb)) for comb in combinations(order, c)]
            comb_counter.update(combs)
            print(f"  Order: {order}, Combos: {combs}")

        print(f"  Comb Counter: {comb_counter}")
        
        # 가장 많이 주문된 조합 찾기
        if comb_counter:
            max_count = max(comb_counter.values())
            print(f"  Max Count: {max_count}")
            if max_count >= 2:
                max_combos = [comb for comb in comb_counter if comb_counter[comb] == max_count]
                print(f"  Max Combos: {max_combos}")
                answer.extend(max_combos)

    return sorted(answer)
