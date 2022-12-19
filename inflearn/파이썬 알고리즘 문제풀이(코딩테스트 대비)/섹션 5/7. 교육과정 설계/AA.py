from collections import deque


need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq: #dq안에 x가 있을 시 참 
            if x != dq.popleft():   #x가 오게 될 시 pop이 되면서 다음 순번을 기다리게 됨 똑같은 값이 오면 if문 통과
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0: #전부 for문 진행 후 print
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
                