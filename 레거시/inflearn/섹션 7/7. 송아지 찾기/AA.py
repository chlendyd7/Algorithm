#BFS 는 레벨 탐색, 큐가 필요함 first in first out
import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
MAX = 10000 # 좌표의  max
ch = [0] * (MAX+1) # 0번부터 생기니 MAX+1
dis = [0] * (MAX+1) # 0번부터 생기니 MAX+1
n,m = map(int,input().split())
ch[n] = 1 # 출발점
dis[n] = 0
dQ = deque()
dQ.append(n)
while True: 
    now = dQ.popleft()
    if now==m:
        break
    for next in (now-1, now+1, now+5): #3 갈래로 뻗음, now-1로 됬다 now+1로, now+5로 3번 돔
        if 1 <= next <= MAX: # 음수좌표 방지, 
            if ch[next]==0: # 방문을 한 좌표 방지
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
                
print(dis[m])