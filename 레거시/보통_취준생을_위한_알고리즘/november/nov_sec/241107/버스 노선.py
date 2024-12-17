from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
bus = []
for i in range(1, n+1):
    a,b = map(int, input().split())
    bus.append((a,-b,i))
bus.sort()
stack1 = deque()
stack2 = deque()
for a,b,i in bus:
    b = -b
    if a < b:
        if not stack1 or stack1[-1][1] < b:
            stack1.append((a,b,i))
    else:
        if not stack2 or stack2[-1][1] < b:
            stack2.append((a,b,i))

while stack1 and stack2:
    if stack1[0][1] <= stack2[-1][1]:
        stack1.popleft()
    elif stack1[-1][0] >= stack2[0][0]:
        stack1.pop()
    else:
        break

print(*sorted(i[2] for i in stack1 + stack2))
