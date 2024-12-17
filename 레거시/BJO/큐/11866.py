# 11866 요세푸스 문제 0
#다시보기
# import sys; input = sys.stdin.readline
# from collections import deque

# n,k = map(int,input().split())
# ls = [i for i in range(1, n+1)]
# odps = []
# ls = deque(ls)
# # list
# for _ in range(n):
#     a = ls[k+1]
#     odps.append(a)
#     ls.remove(a)
#     ls.rotate(k)

# print(odps)
# import sys; input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
deq = deque([i for i in range(1,n+1)])

print('<', end='')

while deq:
    for _ in range(k-1):
        deq.append(deq[0])
        deq.popleft()
    print(deq.popleft(), end='')

    if deq:
        print(', ',end='')
print('>')

