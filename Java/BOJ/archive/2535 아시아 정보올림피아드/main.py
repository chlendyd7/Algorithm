# 나라별 메달 수 2개
from collections import defaultdict


N = int(input())
students = []
for _ in range(N):
    c, n, score = map(int, input().split())
    students.append([c,n,score])

students.sort(key=lambda x:x[2], reverse=True)
check = defaultdict(int)

result = []
for c,n, score in students:
    if len(result) == 3:
        break
    if check.get(c, 0) < 2:
        result.append([c,n])
        check[c] += 1
    else:
        continue

for r in result:
    print(' '.join(map(str, r)))
