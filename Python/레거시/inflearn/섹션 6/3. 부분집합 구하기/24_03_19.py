'''
    트리 구조로 돌아야함
'''

def DFS(v):
    if v==n+1:
        for i in range(n+1):
            if ls[i]==1:
                print(i, end=' ')
        print()
    else:
        ls[v]=1
        DFS(v+1)
        ls[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ls = [0]*(n+1)
    DFS(1)