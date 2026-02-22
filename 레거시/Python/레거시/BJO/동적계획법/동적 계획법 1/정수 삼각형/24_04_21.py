n=int(input())
dy=[]
for i in range(n):
    dy.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(dy[i])):
        if j==0:
            dy[i][j] = dy[i][j]+dy[i-1][j]
        elif j==len(dy[i])-1:
            dy[i][j] = dy[i][j]+dy[i-1][j-1]
        else:
            dy[i][j] = dy[i][j]+max(dy[i-1][j-1], dy[i-1][j])
print(max(dy[n-1]))
