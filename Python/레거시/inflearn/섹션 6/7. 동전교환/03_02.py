def DFS(L,sum):
    global cnt
    if L >= cnt:
        return
    if sum>res:
        return
    if sum==res:
        if L<cnt:
            cnt=L
    else:
        for i in range(n):
            DFS(L+1, sum+ls[i])





if __name__=="__main__":
    n = int(input())
    ls = list(map(int,input().split()))
    res = int(input())
    cnt = 10000000
    ls.sort(reverse=True)
    DFS(0,0)
    print(cnt)
