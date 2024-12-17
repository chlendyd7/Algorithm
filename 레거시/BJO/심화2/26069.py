import sys; input = sys.stdin.readline
from collections import defaultdict




import sys

N = int(sys.stdin.readline())

dance_set = set()

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()
    
    if len(dance_set) == 0 and (a == "ChongChong" or b == "ChongChong"):
        dance_set.add(a)
        dance_set.add(b)
    elif a in dance_set:
        dance_set.add(b)
    elif b in dance_set:
        dance_set.add(a)

print(len(dance_set))




# dance = defaultdict(bool)
# dance['ChongChong'] = True
# cnt = 1

# for _ in range(int(input())):
#     A, B = input().split()
#     if dance[A]:
#         if not dance[B]:
#             dance[B] = True
#             cnt +=1
#     elif dance[B]:
#         dance[A] = True
#         cnt +=1

# print(cnt)
