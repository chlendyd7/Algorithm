'''
    중복순열
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
            ls[k]=i
            DFS(k+1)

n,m=map(int,input().split())
ls=[0]*m
cnt = 0
DFS(0)
print(cnt)