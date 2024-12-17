n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.insert(0,[0,0,0])
arr=sorted(arr, key=lambda x:x[0], reverse=True)
print(arr)
dy=[0]*(n+1)
res=arr[0][1]
dy[1]=arr[0][1]
for i in range(n+1):
    max=0
    for j in range(i-1,-1,-1):
        if arr[j][2]>arr[i][2] and dy[j]>max:
            max=dy[j]
    dy[i]=max+arr[i][1]
    if dy[i]>res:
        res=dy[i]
print(res)