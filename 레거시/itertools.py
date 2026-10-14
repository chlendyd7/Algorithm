from itertools import permutations, combinations, combinations_with_replacement, product

# ────────────────────────────────────────────────
# 선택 가이드
# ┌─────────────┬──────────┬──────────┐
# │             │ 순서 중요 │ 순서 무관 │
# ├─────────────┼──────────┼──────────┤
# │ 중복 없음   │ permutations │ combinations │
# │ 중복 허용   │ product  │ combinations_with_replacement │
# └─────────────┴──────────┴──────────┘
# ────────────────────────────────────────────────

items = [1, 2, 3]
r = 2  # 뽑는 수

# ── 1. 순열 (순서 O, 중복 X) ──────────────────
# 예: [1,2]와 [2,1]이 다름. n개 중 r개 줄 세우기
for p in permutations(items, r):
    print(p)  # (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)

# ── 2. 조합 (순서 X, 중복 X) ──────────────────
# 예: [1,2]와 [2,1]이 같음. n개 중 r개 고르기
for c in combinations(items, r):
    print(c)  # (1,2), (1,3), (2,3)

# ── 3. 중복조합 (순서 X, 중복 O) ─────────────
# 예: 같은 원소 여러 번 뽑기 가능, 순서 무관
for c in combinations_with_replacement(items, r):
    print(c)  # (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)

# ── 4. 중복순열 (순서 O, 중복 O) ─────────────
# 예: 자리마다 같은 원소 가능. product(items, repeat=r)
for p in product(items, repeat=r):
    print(p)  # (1,1), (1,2), ..., (3,3)  총 n^r 가지


# ────────────────────────────────────────────────
# 문제 풀이 템플릿
# ────────────────────────────────────────────────

import sys
input = sys.stdin.readline

def solve():
    _, r = map(int, input().split())
    items = list(map(int, input().split()))

    # TODO: 아래 중 하나 선택
    result = list(permutations(items, r))
    # result = list(combinations(items, r))
    # result = list(combinations_with_replacement(items, r))
    # result = list(product(items, repeat=r))

    for row in result:
        print(*row)

solve()
