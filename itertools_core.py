"""
combinations / permutations / product 핵심 정리

판단 기준:
  순서 중요?  NO  → combinations (or combinations_with_replacement if 중복 허용)
  순서 중요?  YES → permutations (중복 없음) / product (중복 허용)
"""
from itertools import combinations, permutations, product

# ══════════════════════════════════════════════════════
# 개념
# ══════════════════════════════════════════════════════
"""
combinations(iterable, r)
  - 순서 X, 중복 X
  - (1,2) == (2,1)  →  하나만
  - nCr 가지

permutations(iterable, r)
  - 순서 O, 중복 X
  - (1,2) != (2,1)  →  둘 다
  - nPr 가지

product(iterable, repeat=r)
  - 순서 O, 중복 O
  - (1,1) 가능
  - n^r 가지
  - 여러 iterable 넣으면 데카르트 곱
"""

items = [1, 2, 3]
r = 2

print("combinations(r=2):", list(combinations(items, r)))
print("  개수:", len(list(combinations(items, r))))   # 3C2 = 3

print("permutations(r=2):", list(permutations(items, r)))
print("  개수:", len(list(permutations(items, r))))   # 3P2 = 6

print("product(repeat=2): ", list(product(items, repeat=r)))
print("  개수:", len(list(product(items, repeat=r)))) # 3^2 = 9

# ══════════════════════════════════════════════════════
# 판단 연습: 아래 주석 보고 어떤 함수 써야 할지 판단 후 실행
# ══════════════════════════════════════════════════════

print("\n" + "="*50)
print("판단 연습")
print("="*50)

# Q1.
# 5명 중 2명을 뽑아 팀을 만드는 경우의 수
# → 팀이니까 순서 관계없음. (A,B팀 == B,A팀)
people = ['A', 'B', 'C', 'D', 'E']
q1 = list(combinations(people, 2))
print(f"\nQ1 팀 조합 ({len(q1)}가지):", q1[:5], "...")

# Q2.
# 5명 중 회장, 부회장 뽑는 경우의 수
# → 역할이 다르니까 순서 중요. (A회장B부 != B회장A부)
q2 = list(permutations(people, 2))
print(f"\nQ2 임원 순열 ({len(q2)}가지):", q2[:5], "...")

# Q3.
# 0~9 숫자로 만들 수 있는 4자리 PIN (같은 숫자 반복 가능)
# → 순서 O, 중복 O
digits = list(range(10))
q3 = list(product(digits, repeat=4))
print(f"\nQ3 4자리 PIN ({len(q3)}가지): 예) {q3[1234]}")

# Q4.
# [1,2,3,4] 에서 두 수를 골라 합이 5인 쌍 찾기
# → 쌍이니까 순서 무관
arr = [1, 2, 3, 4]
q4 = [(a, b) for a, b in combinations(arr, 2) if a + b == 5]
print(f"\nQ4 합이 5인 쌍:", q4)  # (1,4), (2,3)

# Q5.
# [1,2,3] 수열의 모든 배열 나열 (전체 순열)
# → r 생략하면 전체
q5 = list(permutations([1, 2, 3]))
print(f"\nQ5 전체 순열 ({len(q5)}가지):", q5)

# Q6.
# True/False 스위치 3개의 모든 상태
# → 각 스위치 독립, 중복 허용
q6 = list(product([True, False], repeat=3))
print(f"\nQ6 스위치 상태 ({len(q6)}가지):", q6)

# Q7.
# BFS/DFS에서 상하좌우 방향 벡터
# → (-1,0,1) x (-1,0,1) 데카르트 곱에서 (0,0) 제외
dirs_8 = [(dr, dc) for dr, dc in product([-1, 0, 1], repeat=2) if (dr, dc) != (0, 0)]
dirs_4 = [d for d in dirs_8 if 0 in d]  # 대각선 제거
print(f"\nQ7 4방향:", dirs_4)
print(f"    8방향:", dirs_8)

# Q8.
# 문자열 'ABC'로 만들 수 있는 2글자 단어 (중복 허용)
# → 순서 O, 중복 O
q8 = [''.join(p) for p in product('ABC', repeat=2)]
print(f"\nQ8 2글자 단어 ({len(q8)}가지):", q8)

# ══════════════════════════════════════════════════════
# 헷갈리는 경우 비교
# ══════════════════════════════════════════════════════
print("\n" + "="*50)
print("헷갈리는 케이스")
print("="*50)

"""
'2명 뽑아서 악수' vs '2명 뽑아서 줄 세우기'
  악수: (A,B) == (B,A)  → combinations
  줄세우기: (A,B) != (B,A) → permutations
"""
two = ['A', 'B', 'C']
print("\n악수 (combinations):", list(combinations(two, 2)))   # 3가지
print("줄세우기 (permutations):", list(permutations(two, 2))) # 6가지

"""
같은 숫자 두 번 쓸 수 있는가?
  없음: combinations or permutations
  있음: product
"""
nums = [1, 2, 3]
print("\n중복 없는 2자리:", list(permutations(nums, 2)))  # (1,1) 없음
print("중복 있는 2자리: ", list(product(nums, repeat=2))) # (1,1) 있음
