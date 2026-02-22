from itertools import combinations


def solution(numbers):
    comb = combinations(numbers, 2)
    num_set = set()
    for a,b in comb:
        num_set.add(a + b)
    answer = sorted(num_set)
    print(answer)
    return answer
