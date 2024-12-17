'''
    체크리스트 만들어야함
'''




def DFS(k):
    global cnt
    if k==m:
        for j in range(m):
            print(ls[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ls[k]=i
                ch[i]=1
                DFS(k+1)
                ch[i]=0

n,m = map(int, input().split())
ls=[0]*m
ch=[0]*(n+1)
cnt=0
DFS(0)
print(cnt)