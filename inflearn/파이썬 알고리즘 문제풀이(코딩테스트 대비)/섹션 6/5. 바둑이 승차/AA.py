

def DFS(L, sum):
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L])





if __name__=="__main__":
    c, n = map(int, input().split())
    a=[0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    DFS(0,0)
