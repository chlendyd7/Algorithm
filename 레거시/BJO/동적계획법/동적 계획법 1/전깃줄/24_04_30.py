n=int(input())
ls=[]
dy=[1]*n
for i in range(n):
    a,b = map(int, input().split())
    ls.append((a,b))

ls.sort()
for i in range(1,n):
    for j in range(i):
        if ls[i][1]>ls[j][1]:
            dy[i] = max(dy[i], dy[j]+1)

print(n-max(dy))