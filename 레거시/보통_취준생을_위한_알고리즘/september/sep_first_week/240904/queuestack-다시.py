# https://www.acmicpc.net/problem/24511
from collections import deque
import sys


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))

q = deque([])
for i in range(N):
    if A[i] == 0:
        q.appendleft(B[i])

if not q:
    print(*C)
    sys.exit()

for i in range(M):
    q.append(C[i])
    print(q.popleft(), end=' ')
