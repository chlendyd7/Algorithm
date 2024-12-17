from collections import deque


n=int(input())
ls = deque()
for num in range(1, n+1):
    ls.append(num)

while len(ls)>1:
    ls.popleft()
    ls.append(ls.popleft())

print(ls[0])