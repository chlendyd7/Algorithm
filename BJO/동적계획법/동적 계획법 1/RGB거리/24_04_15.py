n=int(input())
array=[]
dy=[]
for i in range(n):
    array.append(list(map(int,input().split())))
    dy.append([0,0,0])

dy[0]=array[0]
for i in range(1, n):
    for j in range(3):
        if j==0:
            dy[i][j] = min(array[i][j]+dy[i-1][1], array[i][j]+dy[i-1][2])
        if j==1:
            dy[i][j] = min(array[i][j]+dy[i-1][0], array[i][j]+dy[i-1][2])
        if j==2:
            dy[i][j] = min(array[i][j]+dy[i-1][1], array[i][j]+dy[i-1][0])

print(min(dy[n-1]))
