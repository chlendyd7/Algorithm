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
            for comb in combinations(range(4), r):
                key = details[:]
                for idx in comb:
                    key[idx] = '-'
            
            key_str = ' '.join(key)
            info_map[key_str].append(score)
    
    for key in info_map:
        info_map[key].sort()
    
    for q in query:
        condtions = q.replace(" and", "").split()
        target_score = int(condtions.pop())
        target_key= " ".join(condtions)

        scores = info_map[target_key]

        if not scores:
            answer.append(0)
            continue

        start_idx = bisect_left(scores, target_score)
        answer.append(len(scores) - start_idx)
    
    return answer