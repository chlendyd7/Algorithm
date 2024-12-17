n = int(input())
arr=[]
dy=[0]*n
res=0
for i in range(n):
    a,b,c=map(int,input().split())
    arr.append((a,b,c))
arr.sort(reverse=True)
dy[0]=arr[0][1]
res=arr[0][1]
for i in range(n):
    max_h=0
    for j in range(i-1, -1, -1):
        if arr[j][2]>arr[i][2] and dy[j]>max_h:
            max_h = dy[j]
        dy[i]=max_h+arr[i][1]
    res=max(res, dy[i])
print(res)
