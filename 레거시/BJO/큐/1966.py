#1966 프린터 큐
from collections import deque
import sys; input = sys.stdin.readline
#딕셔너리 enumerate
test = int(input())

for i in range(test):
    
    n,m = map(int,input().split())
    score = list(map(int,input().split()))
    q = [(i,idx) for idx,i in enumerate(score)]

    cnt = 0

    while True:
        if q[0][0] == max(q,key = lambda x:x[0][0]):
            cnt +=1
            if q[0][1] == m:
                print(cnt)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))


