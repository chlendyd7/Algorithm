from collections import deque
n = int(input())
ls = [0]*n
for i in range(n):
    ls[i] = i+1

ls = deque(ls)
while len(ls) != 1:
    ls.popleft()
    tmp = ls.popleft()
    ls.append(tmp)

print(ls[0])