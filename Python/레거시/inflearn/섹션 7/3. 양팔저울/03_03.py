def DFS(L,s):
    global res
    if L==k:
        if 0<s<=a:
            res.add(s)
    else:
        DFS(L+1, s+ls[L])
        DFS(L+1, s-ls[L])
        DFS(L+1, s)




if __name__=="__main__":
    k = int(input())
    ls = list(map(int,input().split()))
    a = sum(ls)
    res = set()
    DFS(0,0)
    print(a - len(res))