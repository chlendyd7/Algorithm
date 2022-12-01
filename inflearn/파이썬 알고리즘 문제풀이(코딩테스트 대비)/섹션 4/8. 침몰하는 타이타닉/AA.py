from collections import deque


n, limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p = deque(p) #deque는 앞에서도 뺏다 넣었다 가능 
cnt = 0
while p: #p가 비어있을 때 까지 동작
    if len(p) == 1:
        cnt +=1
        break
    if p[0] + p[-1] > limit: #p의 가장 가벼운, 가장 무거운
        p.pop()
        cnt += 1
    else:
        p.popleft()#p.pop(0) list일 시
        p.pop()
        cnt += 1

print(cnt)

