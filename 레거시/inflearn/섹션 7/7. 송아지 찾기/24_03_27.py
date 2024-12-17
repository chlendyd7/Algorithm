#BFS 는 레벨 탐색, 큐가 필요함 first in first out
import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
MAX = 10000 # 좌표의  max
ch = [0] * (MAX+1) # 0번부터 생기니 MAX+1
dis = [0] * (MAX+1) # 0번부터 생기니 MAX+1
n,m = map(int,input().split())
dq=deque()
ch[n]=1
dis[n]=0
dq.append(n)
while True:
    now = dq.popleft()
    if now==m:
        break
    for next in (now-1, now+1, now+5):
        if 1<=next<=MAX:
            if ch[next]==0:
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])