import sys
from io import StringIO

# ===== 테스트용 입력 & 기대 출력 =====
test_input = """\
5
1 2 2
1 2 3
1 2 4
1 2 5
10 7 1293
"""

expected_output = """\
1
2
2
3
11
"""

T = int(input())
for _ in range(T):
    a, b, n = map(int, input().split())
    cnt = 0
    while not a > n and not b > n:
        if a > b:
            b += a
            cnt += 1
        else:
            a += b
            cnt += 1
    print(cnt)

