n=int(input())
arr=list(map(int,input().split()))
dy=[0]*(n+1)
arr.insert(0,0)
res=0
for i in range(1,n+1):
    cnt=0
    for j in range(i,0,-1):
        if arr[i]>arr[j] and dy[j]>cnt:
            cnt=dy[j]
    dy[i]=cnt+1
    res=max(res,dy[i])
print(res)