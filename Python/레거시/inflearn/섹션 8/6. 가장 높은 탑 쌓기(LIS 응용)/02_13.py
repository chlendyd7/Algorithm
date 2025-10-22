# 파이팅
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.insert(0,0)
dy = [0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j][0]<arr[i][0] and arr[j][2]<arr[i][0] and dy[j][1]>max:
            max += dy[j][1]
    dy[i]=max
    if dy[i]>res:
        res=dy[i]
print(res)
