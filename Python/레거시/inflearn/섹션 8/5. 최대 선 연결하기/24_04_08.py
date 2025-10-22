n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(1,n+1):
    max=0
    for j in range(i-1,0,-1):
        if dy[i]>dy[j] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if res<dy[i]:
        res=dy[i]
print(res)