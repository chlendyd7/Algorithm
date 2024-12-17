from collections import deque


n,m = map(int, input().split())
ls = list(range(1, n+1))
dq = deque(ls)

while dq:
    for _ in range(m-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq.pop())
        
