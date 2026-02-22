def DFS(L, a):
    if L == k:
        if 0<a<=s:
            res.add(a)
    else:
        DFS(L+1, a+G[L])
        DFS(L+1, a-G[L])
        DFS(L+1, a)
        






if __name__ == "__main__":
    k = int(input())
    G = list(map(int,input().split()))
    s = sum(G)
    res = set()
    DFS(0,0)
    print(s-len(res))