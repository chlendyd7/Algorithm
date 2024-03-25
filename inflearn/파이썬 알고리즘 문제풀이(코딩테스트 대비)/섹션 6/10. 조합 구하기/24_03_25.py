'''
    가지를 뻣는다고 생각해야함
    한 가지에 몇 레벨인지 생각
'''
def DFS(L, s):
    global cnt
    if L==m:
        for i in range(m):
            print(ls[i], end=' ')
        print()
        cnt+=1
    
    for i in range(s, n+1):
        ls[L]=i
        DFS(L+1, i+1)



n,m = map(int,input().split())
ls=[0]*(n+1)
cnt = 0
DFS(0,1)