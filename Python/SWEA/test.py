from collections import deque



lst = deque([1,2,3,4,5])
l2 = []
while True:
    if len(l2) < 2:
        l2.append(lst.popleft())
    else:
        break
print(l2)