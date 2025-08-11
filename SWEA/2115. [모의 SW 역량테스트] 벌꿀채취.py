from collections import defaultdict
from itertools import combinations

def get_max_profit(cells, C):
    """해당 구간(M칸)에서 꿀 양 ≤ C 조건 하 최대 수익(제곱합)"""
    M = len(cells)
    max_profit = 0
    for r in range(1, M + 1):
        for comb in combinations(cells, r):
            if sum(comb) <= C:
                profit = sum(x * x for x in comb)
                max_profit = max(max_profit, profit)
    return max_profit

def solution():
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 1. 모든 구간 최대 수익 계산해서 defaultdict 저장
    segment_profit = defaultdict(int)
    for r in range(N):
        for c in range(N - M + 1):
            cells = board[r][c:c + M]
            segment_profit[(r, c)] = get_max_profit(cells, C)

    # 2. 두 구간 조합으로 최대 수익 찾기
    keys = list(segment_profit.keys())
    answer = 0
    for i in range(len(keys)):
        r1, c1 = keys[i]
        p1 = segment_profit[(r1, c1)]
        for j in range(i + 1, len(keys)):
            r2, c2 = keys[j]
            p2 = segment_profit[(r2, c2)]
            # 같은 행이면 겹치면 안됨
            if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
                continue
            answer = max(answer, p1 + p2)

    return answer

T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} {solution()}")
