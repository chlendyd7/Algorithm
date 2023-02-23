import sys
from collections import deque
#2644
input = sys.stdin.readline

N = int(input())
A,B = map(int,input().split())
M = int(input())
boolean = True
result = -1

graph =[[] for i in range(N+1)]

for i in range(M):
    num1, num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
print(graph)
BFS = [0] * (N+1)

def bfs(v):
    q = deque()
    q.append(v) # 7
    BFS[v] = 1 # BFS[v] = 1

    while q:
        v = q.popleft() # v=7
        for i in graph[v]: #i = graph[7] == 2
            if not BFS[i]: #BFS[2]
                BFS[i] += (BFS[v]+1) #BFS[2] += BFS[7]+1
                q.append(i)
bfs(A)

if BFS[B] != 0:
    print(BFS[B]-1)
else:
    print(-1)
