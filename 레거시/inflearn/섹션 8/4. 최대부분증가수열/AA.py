n=int(input())
arr=list(map(int,input().split()))
res =0
dy=[0]*(n+1)
arr.insert(0,0)
dy[1]=1
for i in range(n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
        dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)
