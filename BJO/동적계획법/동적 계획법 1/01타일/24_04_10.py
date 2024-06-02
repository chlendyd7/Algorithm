'''
    조건:
        1. 00은 붙어야한다
        2. 1은 자유로히
'''
n=int(input())
cnt=0
def DFS(L):
    global cnt
    if L==n:
        cnt+=1
        return
    else:
        if L+2<=n:
            DFS(L+2)
        DFS(L+1)
DFS(0)
print(cnt%15746)