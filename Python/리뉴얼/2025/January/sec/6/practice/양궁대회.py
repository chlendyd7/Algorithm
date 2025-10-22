from itertools import combinations_with_replacement


def solution(n, info):
    max_diff = 0
    answer = [-1]

    for comb in combinations_with_replacement(range(11), n):
        lion = [0] * 11
        for c in comb:
            lion[10 - c] += 1
        
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if info[i] >= lion[i]:
                apeach_score += 10 - i
            else:
                lion_score += 10 - i

        diff = lion_score - apeach_score

        if diff > max_diff or (diff == max_diff and lion[::-1] > answer[::-1]):
            max_diff = diff
            answer = lion
        

    return answer if max_diff > 0 else [-1]
