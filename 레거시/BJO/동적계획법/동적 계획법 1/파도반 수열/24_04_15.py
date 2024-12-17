dy=[0]*101
dy[1]=1
dy[2]=1
dy[3]=1
for i in range(4, 101):
    dy[i] = dy[i-2]+dy[i-3]

n=int(input())
for i in range(n):
    print(dy[int(input())])