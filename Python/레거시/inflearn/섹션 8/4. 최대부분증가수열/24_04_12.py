n=int(input())
ls=list(map(int,input().split()))
ls.insert(0,0)
ch=[0]*(n+1)
ch[1]=1
res=0
for i in range(2,n+1):
    count=0
    for j in range(i,0,-1):
        if ls[i]>ls[j] and ch[j]>count:
            count=ch[j]
    ch[i]=count+1
    res=max(res,ch[i])

print(res)