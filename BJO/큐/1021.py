# 1021 회전하는 큐
from collections import deque
import sys; input = sys.stdin.readline

n,m = map(int,input().split())
qu = deque(range(1,n+1))
nums = list(map(int,input().split()))
cnt = 0
for num in nums:
    while qu:
        if qu[0] == num:
            qu.popleft()
            break
        if qu.index(num) <= len(qu) //2:
            qu.append(qu.popleft())
        else:
            qu.appendleft(qu.pop())
        cnt +=1
print(cnt)
