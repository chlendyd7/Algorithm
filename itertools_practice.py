"""
itertools 알고리즘 연습
"""
from itertools import (
    combinations, permutations, combinations_with_replacement, product,
    accumulate, chain, groupby, compress, islice, pairwise,
    count, cycle, repeat, dropwhile, takewhile,
)
import operator

# ──────────────────────────────────────────────
# 1. combinations — 조합 nCr (순서 무관, 중복 없음)
# ──────────────────────────────────────────────
arr = [1, 2, 3, 4]

print("=== combinations ===")
print(list(combinations(arr, 2)))
# [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

# 활용: 두 원소 합이 짝수인 쌍
even_pairs = [(a, b) for a, b in combinations(arr, 2) if (a + b) % 2 == 0]
print("짝수 합 쌍:", even_pairs)

# ──────────────────────────────────────────────
# 2. permutations — 순열 nPr (순서 관련, 중복 없음)
# ──────────────────────────────────────────────
print("\n=== permutations ===")
print(list(permutations([1, 2, 3], 2)))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 활용: 방문 순서가 다른 경로 탐색
nodes = ['A', 'B', 'C']
routes = list(permutations(nodes))
print("가능한 경로:", routes)

# ──────────────────────────────────────────────
# 3. combinations_with_replacement — 중복 조합 nHr
# ──────────────────────────────────────────────
print("\n=== combinations_with_replacement ===")
print(list(combinations_with_replacement([1, 2, 3], 2)))
# [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

# ──────────────────────────────────────────────
# 4. product — 중복 순열 / 데카르트 곱
# ──────────────────────────────────────────────
print("\n=== product ===")

# 중복 순열: repeat 인자 사용
print(list(product([0, 1], repeat=3)))  # 3비트 모든 경우
# [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

# 활용: 2D 그리드 모든 칸
grid = [(r, c) for r, c in product(range(3), range(3))]
print("3x3 그리드:", grid)

# 활용: 여러 옵션 조합 (브루트포스)
sizes = ['S', 'M', 'L']
colors = ['red', 'blue']
print(list(product(sizes, colors)))

# ──────────────────────────────────────────────
# 5. accumulate — 누적 연산 (prefix sum 등)
# ──────────────────────────────────────────────
print("\n=== accumulate ===")
nums = [1, 2, 3, 4, 5]

# prefix sum
prefix = list(accumulate(nums))
print("prefix sum:", prefix)  # [1,3,6,10,15]

# prefix max
prefix_max = list(accumulate(nums, max))
print("prefix max:", prefix_max)  # [1,2,3,4,5]

# prefix product
prefix_prod = list(accumulate(nums, operator.mul))
print("prefix product:", prefix_prod)  # [1,2,6,24,120]

# 활용: 구간 합 O(1) 쿼리
def range_sum(prefix, l, r):  # 0-indexed
    return prefix[r] - (prefix[l - 1] if l > 0 else 0)

print("구간합 [1,3]:", range_sum(prefix, 1, 3))  # 2+3+4=9

# ──────────────────────────────────────────────
# 6. chain — 여러 이터러블 이어붙이기
# ──────────────────────────────────────────────
print("\n=== chain ===")
a, b, c = [1, 2], [3, 4], [5, 6]
print(list(chain(a, b, c)))  # [1,2,3,4,5,6]

# 2D 리스트 평탄화
matrix = [[1, 2], [3, 4], [5, 6]]
flat = list(chain.from_iterable(matrix))
print("flatten:", flat)  # [1,2,3,4,5,6]

# ──────────────────────────────────────────────
# 7. pairwise — 인접 쌍 (Python 3.10+)
# ──────────────────────────────────────────────
print("\n=== pairwise ===")
seq = [1, 4, 2, 8, 5]
print(list(pairwise(seq)))  # [(1,4),(4,2),(2,8),(8,5)]

# 활용: 인접 차이 계산
diffs = [b - a for a, b in pairwise(seq)]
print("인접 차이:", diffs)

# ──────────────────────────────────────────────
# 8. groupby — 연속된 같은 값 그룹화 (정렬 후 사용!)
# ──────────────────────────────────────────────
print("\n=== groupby ===")
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# 활용: 런 길이 인코딩
s = "aaabbbccdddd"
rle = [(k, sum(1 for _ in g)) for k, g in groupby(s)]
print("RLE:", rle)  # [('a',3),('b',3),('c',2),('d',4)]

# ──────────────────────────────────────────────
# 9. compress — 마스크로 필터링
# ──────────────────────────────────────────────
print("\n=== compress ===")
data = ['a', 'b', 'c', 'd', 'e']
mask = [1, 0, 1, 0, 1]
print(list(compress(data, mask)))  # ['a','c','e']

# ──────────────────────────────────────────────
# 10. takewhile / dropwhile — 조건 기반 슬라이싱
# ──────────────────────────────────────────────
print("\n=== takewhile / dropwhile ===")
nums = [1, 2, 3, 4, 1, 2]
print(list(takewhile(lambda x: x < 4, nums)))  # [1,2,3]  — 조건 깨지면 즉시 중단
print(list(dropwhile(lambda x: x < 4, nums)))  # [4,1,2] — 조건 깨진 이후부터

# ──────────────────────────────────────────────
# 11. islice — 이터레이터 슬라이싱 (메모리 효율)
# ──────────────────────────────────────────────
print("\n=== islice ===")
gen = (x ** 2 for x in range(1000))
print(list(islice(gen, 5, 10)))  # [25,36,49,64,81] (5~9번째)

# ──────────────────────────────────────────────
# 12. 실전 패턴 모음
# ──────────────────────────────────────────────
print("\n=== 실전 패턴 ===")

# 부분집합 (2^n): product([0,1], repeat=n)
def subsets(arr):
    n = len(arr)
    for mask in product([0, 1], repeat=n):
        yield [arr[i] for i, bit in enumerate(mask) if bit]

print("부분집합:", list(subsets([1, 2, 3])))

# 모든 nCr 경우 브루트포스 최솟값
arr = [3, 1, 4, 1, 5, 9]
min_sum = min(a + b for a, b in combinations(arr, 2))
print("최소 두 원소 합:", min_sum)  # 1+1=2

# 격자 BFS 방향: product([-1,0,1], repeat=2) 에서 (0,0) 제외
dirs = [(dr, dc) for dr, dc in product([-1, 0, 1], repeat=2) if (dr, dc) != (0, 0)]
print("8방향:", dirs)

# 4방향만: compress로 선택
dirs4 = list(compress([(-1,0),(0,-1),(0,1),(1,0)], [1,1,1,1]))
print("4방향:", dirs4)
