def DFS(depth, max):
    global result
    if max>c:
        return
    if max < c and result<max:
        result=max
    if depth==n:
        if max>result:
            result=max
    else:
        DFS(depth+1, max+ls[depth])
        DFS(depth+1, max)


if __name__=='__main__':
    c, n=map(int, input().split())
    result=0
    ls=[]
    for _ in range(n):
        ls.append(int(input()))
    DFS(0,0)
    print(result)