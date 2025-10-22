from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        comb_counter = Counter()

        for order in orders:
            combs = [''.join(comb) for comb in combinations(order, c)]
