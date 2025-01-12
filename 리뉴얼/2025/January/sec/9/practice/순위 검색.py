from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    info_map = defaultdict(list)

    for person in info:
        details = person.split()
        score = int(details.pop())
        for r in range(5):
            for combs in combinations(range(4), r):
                key = details[:]
                for idx in comb:
                    key[idx] = '-'
                info_map[' '.join(key)].append(score)
    
    for key in info_map:
            info_map[key].sort()

    for q in query:
        conditions = q.replace(' and', '').split()
        target_score = int(conditions.pop())
        target_key = ' '.join(conditions)

        scores = info_map[target_key]

        if not scores:
            answer.append(0)
            continue

        start_idx = bisect_left(scores, target_score)
        answer.append(len(scores) - start_idx)
   
    return answer
