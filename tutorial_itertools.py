# 순열: 순서를 고려해서 뽑는 경우
from itertools import permutations

arr = [1, 2, 3]
for p in permutations(arr, 2):
    print(p)

# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)


# 조합: 순서를 고려하지 않고 뽑는 경우
from itertools import combinations

arr = [1, 2, 3]
for c in combinations(arr, 2):
    print(c)

# (1, 2)
# (1, 3)
# (2, 3)


# 중첩 루프 + 중복 허용 (곱집합)
from itertools import product

for p in product([0, 1], repeat=3):
    print(p)

# 출력
# (0, 0, 0)
# (0, 0, 1)
# (0, 1, 0)
# (0, 1, 1)
# (1, 0, 0)
# (1, 0, 1)
# (1, 1, 0)
# (1, 1, 1)