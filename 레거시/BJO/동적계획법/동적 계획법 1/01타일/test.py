n=int(input())
dy=[0]*100001
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i] = (dy[i-1]+dy[i-2])%15746
print(dy[n])