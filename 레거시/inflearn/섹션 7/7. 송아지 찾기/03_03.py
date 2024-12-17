#BFS
from collections import deque
MAX = 100000
ch = [0] *(MAX+1)
dis = [0] *(MAX+1)
n,m = map(int,input().split())
ch[n]=1
dis[n] = 0 #거리
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): # for문 3방향으로 돔
        if 0<next<=MAX:
            if ch[next] ==0:
                dQ.append(next)
                ch[next] = 1
                dis[next]=dis[now]+1
print(dis[m])






# def DFS(L, x):
#     global cnt
#     if L==e:
#         if x < cnt:
#             cnt = x
#     if x>cnt:
#         return
#     else:
#         DFS(L+1, x+1)
#         DFS(L+5, x+1)
#         DFS(L-1, x+1)



# if __name__=="__main__":
#     s,e = map(int,input().split())
#     cnt = 100000
#     DFS(s,0)
#     print(cnt)