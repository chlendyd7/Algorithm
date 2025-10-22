from collections import deque


n, m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
ls = deque(ls)
cnt = 0
while ls:
    if len(ls) == 1:
        cnt +=1
        break
    if ls[0] + ls[-1] > m:
        ls.pop()
        cnt+=1
    else:
        ls.pop()
        ls.popleft()
        cnt+=1

print(cnt)