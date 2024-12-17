from collections import deque

a, b = map(int, input().split())
dq = list(range(1, a+1))
dq = deque(dq)

while dq:
    for _ in range(b-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    
    if len(dq)==1:
        print(dq[0])
        dq.popleft()