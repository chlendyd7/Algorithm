n=int(input())
dy=[0]*1001
ls=list(map(int,input().split()))
ls.insert(0,0)

for i in range(1, n+1):
    for j in range(i):
        if ls[i] > ls[j]:
            dy[i] = max(dy[i], dy[j]+1)

print(max(dy))