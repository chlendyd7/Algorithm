from collections import deque


need = input()
cnt = int(input())
for i in range(cnt):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x!= dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))        
    