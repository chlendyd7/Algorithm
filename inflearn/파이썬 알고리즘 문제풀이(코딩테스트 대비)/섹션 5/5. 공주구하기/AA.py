from collections import deque
a, b = map(int, input().split())
q = list(range(1, a+1))
# for _ in range(1, a+1):
#     q.append(_)
dq = deque(q)

while dq:
    for _ in range(b-1): # 하나 작은 상태까지 돌아감 ex) 4 = 0,1,2
        cur = dq.popleft() # 왼쪽에서 하나씩 빼 오른쪽으로 append
        dq.append(cur)
    dq.popleft() # b번째의 숫자가 pop됨
    if len(dq)==1: 
        print(dq[0])
        dq.popleft()