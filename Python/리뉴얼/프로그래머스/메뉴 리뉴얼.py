from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = Counter()

        for order in orders:
            combs = [''.join(sorted(comb)) for comb in combinations(order, c)]
            comb_counter.update(combs)
        

        if comb_counter:
            max_count = max(comb_counter.values())
            if max_count >= 2:
                max_combos = [comb for comb in comb_counter if comb_counter[comb] == max_count]
                answer.extend(max_combos)
    return sorted(answer)
