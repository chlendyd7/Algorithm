from collections import deque


n, limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p = deque(p) #deque는 앞에서도 뺏다 넣었다 가능 
cnt = 0
while p: #p가 비어있을 때 까지 동작
    if len(p) == 1: # 한명이면 그냥 1개쓰고 break
        cnt +=1
        break
    if p[0] + p[-1] > limit: #p의 가장 무거운 사람과 탈 수 있는 사람은 가장 가벼운 사람일 가능성이 높음
        p.pop() # limit 넘어가면 혼자 타고가야지~
        cnt += 1
    else:
        p.popleft()#p.pop(0) list일 시 둘이만 타고 갈 수 있다 가정이 있음
        p.pop()
        cnt += 1  

print(cnt)

